#description 
#this file recieves crypto price data from coinmarketcap api and updates the same on a local mongodb database

import requests,time
from datetime import datetime
from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"
KEY = "0912f13f-3d92-450c-927f-d343e787baea"
parameters = {
    'start': '1',
    'limit': '5',
    'convert':'INR'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': KEY
}
URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"


def api_call():
    global URL,parameters,headers
    result = requests.get(URL,params=parameters,headers=headers).json()
    time = datetime.now()
    time = time.strftime("%d/%m/%Y %H:%M:%S")
    btc = {'name':result['data'][0]['name'],'symbol':result['data'][0]['symbol'],'price':round(result['data'][0]['quote']['INR']['price'],2)}
    eth = {'name':result['data'][1]['name'],'symbol':result['data'][1]['symbol'],'price':round(result['data'][1]['quote']['INR']['price'],2)} 
    usdt = {'name':result['data'][2]['name'],'symbol':result['data'][2]['symbol'],'price':round(result['data'][2]['quote']['INR']['price'],2)}
    usdc = {'name':result['data'][3]['name'],'symbol':result['data'][3]['symbol'],'price':round(result['data'][3]['quote']['INR']['price'],2)}
    bnb = {'name':result['data'][4]['name'],'symbol':result['data'][4]['symbol'],'price':round(result['data'][4]['quote']['INR']['price'],2)}
    return {
        'time':time,
        'btc':btc,
        'eth':eth,
        'usdt':usdt,
        'usdc':usdc,
        'bnb':bnb
    }    

client = MongoClient(MONGO_URL)
db = client['crypto_price']
collection = db['prices']


print("UPDATING DATABASE")
while True:
    time.sleep(5)
    collection.insert_one(api_call())