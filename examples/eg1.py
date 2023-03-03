#Description
#This is a example program showing use of observables, pipe() and subscribe()
import rx
import json
from rx import operators as ops
def filternames(x):
   if (x["name"].startswith("E")):
      return x["name"]
   else :
      return ""
file = open("users.json")
y = json.load(file)
source = rx.from_(y)
case1 = source.pipe(
   ops.filter(lambda c: filternames(c)),
   ops.map(lambda a:a["name"])
)

case1.subscribe(
   on_next = lambda i: print("Got - {0}".format(i)),
   on_error = lambda e: print("Error : {0}".format(e)),
   on_completed = lambda : print("Job Done!")
)

