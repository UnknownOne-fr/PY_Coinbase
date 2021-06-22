import os

import discord
import config_api
import coinbase_functions

from coinbase_functions import user_name_coinbase, part_wallet_content, full_wallet_content
from coinbase.wallet.client import Client
from dotenv import load_dotenv

# qqch dans les parenthèses de laod_dotenv() car le fichier s'appelle pas '.env' comme c'est le cas
# par défaut car ici c'est le nom de l'env virtuel donc on l'appelle config (il comprend que le fichier
# est dans le fichier courant -> permet de pas déployer le fichier config sur git et donner l'accès au bot
load_dotenv(dotenv_path="config")

# Discord
# Environment variables
default_intents = discord.Intents.default()
default_intents.members = True
# New Discord instance
client = discord.Client(intents=default_intents)


# Define a client action on Discord : Bot connexion to channel
@client.event
async def on_ready():
    print("Le bot est prêt.")


# Define a client action on Discord : client message
@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong")  # ,delete_after=5)

    # Delete messages in channel
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()

        for each_message in messages:
            await each_message.delete()

    # Show the list of key from dictionary
    if message.content.startswith("!key"):
        await message.channel.send("Liste des cryptos disponibles actuellement :")
        for keywords in sorted(coinbase_functions.key):
            await message.channel.send(f"\t- {keywords.capitalize()}")

    # Show all currencies with last sell price
    if message.content.startswith("!all"):
        await message.channel.send("Résumé de la valeur de toutes les cryptos disponibles :")
        for keywords in sorted(coinbase_functions.key):
            await message.channel.send(
                f"{keywords.capitalize()} ({coinbase_functions.liste_crypto_coinbase[keywords]}) "
                f": {coinbase_functions.spot_price_coinbase(keywords)} €")

    # Show unique currency with las sell price
    for keywords in sorted(coinbase_functions.key):
        if message.content.startswith(f">{keywords.lower()}_price"):
            await message.channel.send(
                f"Cours actuel du {keywords.capitalize()} ({coinbase_functions.liste_crypto_coinbase[keywords]}) "
                f": {coinbase_functions.spot_price_coinbase(keywords)} €")

    # Show part wallet content for a customer
    for keywords in sorted(coinbase_functions.key):
        if message.content.startswith(f">{keywords.lower()}_wallet"):  # {user_name_coinbase.lower()}
            for elements in part_wallet_content(keywords):
                await message.channel.send(f"\t{elements}")

    # Show full wallet content for a customer
    if message.content.startswith(f"!full_wallet"):  # {user_name_coinbase.lower()}
        for elements in full_wallet_content(user_name_coinbase):
            await message.channel.send(elements)


# Define a client action on Discord : new channel member
@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel('XXXXXXXXXXXXXX') # replace 'XXXXXXXXXXXXXX' by channel id
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")


# Environment variable to access to config file
client.run(os.getenv("TOKEN"))
