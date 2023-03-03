#Description
#This is a example program showing the use concurrency for having multiple observers and subscribers using subscribe_on() operator.
import time,random,os,threading
import multiprocessing

import rx 
from rx import operators as ops
from rx.scheduler import ThreadPoolScheduler

#calculating cpu count
cpus = multiprocessing.cpu_count()
thread_pool_scheduler = ThreadPoolScheduler(cpus)


def delay(value):
   #print("Waiting")
   time.sleep(random.randint(1,20)*0.1)
   #os.system("cls")
   return value

#first observable
rx.of(1,2,3,4,5).pipe(
   ops.map(lambda s: delay(s)),
   ops.subscribe_on(thread_pool_scheduler) #opertor to run in parallel
).subscribe(
   lambda s:print("Task 1 :{}".format(s)),
   lambda e: print(e)
)

#second observable
rx.range(1,5).pipe(
   ops.map(lambda s: delay(s)),
   ops.subscribe_on(thread_pool_scheduler)
).subscribe(
   lambda s: print("From Task 2: {0}".format(s)),
   lambda e: print(e)
)

print("threads:",threading.active_count())
