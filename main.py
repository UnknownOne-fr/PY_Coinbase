import hashlib
import hmac
import os

import coinbase.wallet.client
# import discordBot
import requests
import time

import coinbase_functions
import config_api
import config_user

import discord
from dotenv import load_dotenv
from requests.auth import AuthBase
from coinbase.wallet.client import Client
# from discordBot import on_message, sell_price_coinbase, liste_crypto_coinbase

# Coinbase
# Environment variables
api_key = config_api.api_keys.get("API_KEY")
api_secret = config_api.api_keys.get("API_SECRET")
# New Coinbase instance
client = Client(api_key, api_secret)


# New Coinbase variables
currencies_list = coinbase_functions.key


# Load specific user : here TDE
user = client.update_current_user(name=config_user.user_settings.get("name"))


total = 0
message = []
accounts = client.get_accounts()


for wallet in accounts.data:
    #print(f"Wallet {wallet}")
    message.append(str(wallet['name']) + ' ' + str(wallet['native_balance']))
    value = str(wallet['native_balance']).replace('EUR', '')
    total += float(value)
    print(str(wallet['name']))
    print(total)
message.append('Total Balance: ' + 'EUR ' + str(total))
print('\n'.join(message))

# print(f"Buy price {buy_price}")
# print(f"Sell price {sell_price}")
# print(f"User {user}")
