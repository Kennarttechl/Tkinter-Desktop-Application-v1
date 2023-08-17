"""HTTP Request Methods
GET
POST
PUT
HEAD
DELETE
PATCH
OPTIONS


GET.....is used to request data from a specified resource
POST....is used to send data to a server to create/update a resource


requests: module help us to the get the data from any link
Jason module helps us to parse the data into human readable format
"""
import json
import requests


coins = [
    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 3200,
    },

    {
        "symbol": "BTC",
        "amount_owned": 2,
        "price_per_coin": 3200,
    }
]


try:
    api_request = requests.get('http://127.0.0.1:5000/items')
    api = json.loads(api_request.content)
    print(api)
except:
    print('Response not available')


try:
    api_request = requests.get('http://127.0.0.1:5000/items_')
    api = json.loads(api_request.content)
    print(api)
except:
    print('Response not available')

   