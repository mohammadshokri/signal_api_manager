from kucoin.client import Client
import ora_db

ora_db.setSignal()

api_key ='62920c331ed13900011b31b1'
api_secret ='cbabe742-a224-430c-a1a7-9620cedfb044'
api_passphrase ='Kk12345678'


# create_limit_order(symbol, side, price, size,
#     client_oid=None, remark=None, time_in_force=None, stop=None, stop_price=None, stp=None, cancel_after=None,
#                    post_only=None, hidden=None, iceberg=None, visible_size=None)

# order = client.create_market_order('SLP-USDT', Client.SIDE_BUY,  size=100)

# order= client.get_order('6461f2f509b21c0001f9d6b3')
# order= client.cancel_order('6461fa96a18dbe0001f96c98')
# client = Client(api_key, api_secret, api_passphrase)
# order = client.cancel_all_orders(symbol='BTC-USDT')
#
# order= client.create_limit_order(symbol='BTC-USDT',client_oid='client_111',side= Client.SIDE_BUY, price='22000', size=0.00001)
# '6461fa96a18dbe0001f96c98'

# client = Client("api-key", "api-secret", "api-passphrase", {"verify": False, "timeout": 20})