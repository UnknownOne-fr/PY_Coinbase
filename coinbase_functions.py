import config_api

from coinbase.wallet.client import Client

# Coinbase
# Environment variables
api_key = config_api.api_keys.get("API_KEY")
api_secret = config_api.api_keys.get("API_SECRET")
# New Coinbase instance
client_coinbase = Client(api_key, api_secret)

# Dictionary to upgrade with all crypto currencies available
liste_crypto_coinbase = {
    'bitcoin': 'BTC-EUR',
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
