a = [23,12,44,51,68,88,100]
import time
for i in a:
    time.sleep(0.1)
    if i > 50: 
        print("CPU USAGE IS HIGH - {},TURNING UP FAN ".format(i))
