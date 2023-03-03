#description
#This file reads crypto price data from a local mongodb database and sends it to its subscribers

from pymongo import MongoClient
import rx,time
from rx import operators as ops
from rx.subject import Subject


MONGO_URL = "mongodb://localhost:27017"
REPLAY = 0



#connecting to db
client = MongoClient(MONGO_URL)
collection = client['crypto_price']['prices']

def db_read():
    global collection
    data = []
    for i in collection.find({},{'_id':0}):
        data.append(i)
    return data

subject = Subject()
subject.subscribe(
    on_next= lambda s:print("At {} BITCOIN was {}".format(s[-1]['time'],s[-1]['btc']['price']))
) 
subject.subscribe(
    on_next= lambda s:print("At {} ETHEREUM was {}".format(s[-1]['time'],s[-1]['eth']['price']))
) 
subject.subscribe(
    on_next= lambda s:print("At {} TETHER was {}".format(s[-1]['time'],s[-1]['usdt']['price']))
) 
subject.subscribe(
    on_next= lambda s:print("At {} BNB was {}".format(s[-1]['time'],s[-1]['bnb']['price']))
) 
subject.subscribe(
    on_next= lambda s:print("At {} USD COIN was {}\n-----------------------------------\n".format(s[-1]['time'],s[-1]['usdc']['price']))
) 
while True:
    time.sleep(1)
    subject.on_next(db_read())