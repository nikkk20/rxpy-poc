#Description
#This is a program which checks for the cpu usage in real time and stores it into a json file in real time
#this program is used to provide a continious data stream of cpu usage for usage in other programs
 

import psutil,time,threading,json
from datetime import datetime
now = datetime.now()

with open("usage.json","w") as file:
            json.dump([{"count":now.strftime("%H:%M:%S"),"usage":psutil.cpu_percent()}],file,indent=4)
def cpu_usage():
    while True: 
        time.sleep(0.5)
        now = datetime.now()
        usage = {"count":now.strftime("%H:%M:%S"),"usage":psutil.cpu_percent(),"freq":psutil.cpu_freq()}
        with open("usage.json") as file:
            data = json.load(file)
        data.append(usage)
        print(usage)
        with open("usage.json","w") as file:
            json.dump(data,file,indent=4)
thread1 = threading.Thread(target=cpu_usage)
thread1.start()