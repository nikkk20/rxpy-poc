#Description
# this file reads data from a mongodb database on the localhost and uses RxPy to process the data and return the output

import pymongo
from pymongo import MongoClient
import json
from rx.subject import Subject
import rx,time,threading
from rx import operators as ops
# creating client onject
data = []
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['sales']
coll = db['salesdata']
result = coll.find({},{"_id":0})
for i in result:
    data.append(i)
#vreating subject
subject = Subject()
subject.pipe(
    ops.filter(lambda s:s['couponUsed'] == True),
    ops.map(lambda e: e['customer']['email'])
).subscribe(
    on_next=lambda s: print("Got - {}".format(s)),
    on_completed=lambda :print("Done") 
)
def data_recv():
    global data,subject
    for i in range(0,len(data)):
        time.sleep(0.5)
        subject.on_next(data[i])
    subject.on_completed()
threading.Thread(target=data_recv).start()