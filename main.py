from kucoin.client import Client

api_key ='62920c331ed13900011b31b1'
api_secret ='cbabe742-a224-430c-a1a7-9620cedfb044'
api_passphrase ='Kk12345678'

client = Client(api_key, api_secret, api_passphrase)
# create_limit_order(symbol, side, price, size,
#     client_oid=None, remark=None, time_in_force=None, stop=None, stop_price=None, stp=None, cancel_after=None,
#                    post_only=None, hidden=None, iceberg=None, visible_size=None)

# order = client.create_market_order('SLP-USDT', Client.SIDE_BUY,  size=100)

# order= client.get_order('6461f2f509b21c0001f9d6b3')
order= client.get_order_by_client_oid('client_1')

print(order)
# order= client.cancel_order('6461fa96a18dbe0001f96c98')

# order= client.create_limit_order('SLP-USDT',client_oid='client_1',side= Client.SIDE_SELL, price='0.0023', size=100)
# '6461fa96a18dbe0001f96c98'
print(order)

# client = Client("api-key", "api-secret", "api-passphrase", {"verify": False, "timeout": 20})