#Description
#This is a program which collects cpu usage information in real time 
#cpu_usage.py needs to be running for this program to function as intended
#This program uses rxpy to process the incoming stream of data and give necessary results
#it filters out and prints the cpu usage only when it is above 10% this can be changed accordingly in line number 17
 

import rx,json,time,threading
from rx import operators as ops
from rx.subject import Subject

#creating the subject
subject = Subject()

#first subscriber
subject.pipe(
    ops.filter(lambda i: i["usage"]> 10.0),
    ops.map(lambda s: s["usage"])
).subscribe(
    on_next=lambda s: print("1st Subscriber got - {}".format(s))
)

#function to read json file
def jsonreader():
    while True:
        time.sleep(0.8)
        with open("usage.json") as f:
            data = json.load(f)
        global subject
        subject.on_next(data[-1])
        
        

thread1 = threading.Thread(target=jsonreader)
thread1.start()
    
