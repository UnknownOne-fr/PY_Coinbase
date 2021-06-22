import os

from coinbase import wallet

import config_api
import config_user

from coinbase.wallet.client import Client

# Coinbase
# Environment variables -> penser à externaliser pour ouvrir le bot aux autres postes et surtout pour full_wallet funct
api_key = config_api.api_keys.get("API_KEY")
api_secret = config_api.api_keys.get("API_SECRET")
# New Coinbase instance
client_coinbase = Client(api_key, api_secret)

# Load specific user : here TDE
user_coinbase = client_coinbase.update_current_user(name=config_user.user_settings.get("name"))
user_name_coinbase = user_coinbase.get("name")

# Dictionary to upgrade with all crypto currencies available
liste_crypto_coinbase = {
    'bitcoin': 'BTC-EUR',  # initially 'BTC-EUR'
    'basic': 'BAT-EUR',
    'cardano': 'ADA-EUR',
    'aave': 'AAVE-EUR',
    'decentraland': 'MANA-EUR',
    'dogecoin': 'DOGE-EUR',
    'yearn': 'YFI-EUR',
    'stellar': 'XLM-EUR'
}

# Key list from dictionary
key = []
for keys in liste_crypto_coinbase:
    key.append(keys)


# Function that return the sell price of a specific crypto
def sell_price_coinbase(crypto):
    sell_price = client_coinbase.get_sell_price(currency_pair=f'{liste_crypto_coinbase[crypto]}')
    return sell_price.get('amount')


# Function that return the sell price of a specific crypto
def buy_price_coinbase(crypto):
    buy_price = client_coinbase.get_buy_price(currency_pair=f'{liste_crypto_coinbase[crypto]}')
    return buy_price.get('amount')


# Function that return the sell price of a specific crypto
def spot_price_coinbase(crypto):
    spot_price = client_coinbase.get_spot_price(currency_pair=f'{liste_crypto_coinbase[crypto]}')
    return spot_price.get('amount')


# Function that return a partly wallet content
def part_wallet_content(crypto):
    message = []
    accounts = client_coinbase.get_accounts(limit=100)

    for wallets in accounts.data:
        crypto_acronym_name = str(wallets.get("balance").get("currency"))  # Return 'XXX'
        crypto_acronym_value = str(wallets.get("balance").get("amount"))
        value_fiat = str(wallets['native_balance']).replace('EUR ', '')

        if value_fiat != "0.00" and crypto_acronym_name in liste_crypto_coinbase.get(crypto):
            message.append(f"{crypto.capitalize()} : {crypto_acronym_value} ({crypto_acronym_name}) = {value_fiat} €")
        else:

            continue
    if not message:
        message.append(f"Vous ne possèdez pas de '{crypto.capitalize()}' dans votre portefeuille")
    return message


# Function that return the full wallet content
def full_wallet_content(crypto):
    total_balance = 0
    message = []
    accounts = client_coinbase.get_accounts(limit=100)

    message.append(f"Contenu du portefeuille de {user_name_coinbase} :")

    for wallets in accounts.data:
        crypto_acronym_name = str(wallets.get("balance").get("currency"))
        crypto_acronym_value = str(wallets.get("balance").get("amount"))
        value_fiat = str(wallets['native_balance']).replace('EUR ', '')

        if value_fiat != "0.00":
            message.append(f"- {crypto_acronym_value} ({crypto_acronym_name}) = {value_fiat} €")
        total_balance += float(value_fiat)
    message.append(f"Valeur totale : {total_balance} €")
    return message
