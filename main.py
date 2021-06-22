# import discordBot

from coinbase.wallet.client import Client

import coinbase_functions
import config_api
import config_user

# from discordBot import on_message, sell_price_coinbase, liste_crypto_coinbase

# Coinbase
# Environment variables
api_key = config_api.api_keys.get("API_KEY")
api_secret = config_api.api_keys.get("API_SECRET")

# New Coinbase instance
client = Client(api_key, api_secret)

# New Coinbase variables
currencies_list = coinbase_functions.key

# Load account balance
'''
Il faudra créer un dictionnaire pour stocker les valeurs du portefeuille et un autre pour celles non détenues
'''

# Load specific user : here TDE
user = client.update_current_user(name=config_user.user_settings.get("name"))
user_name = user.get("name")
