#Description
#This is a example program showing observable functions
from rx import create
def test_observable(observer,scheduler):
    observer.on_next("Hello")
    observer.on_completed()
source = create(test_observable)
source.subscribe(
    on_next=lambda i: print("Got - {0}".format(i)),
    on_error=lambda e: print("Got - {0}".format(e)),
    on_completed=lambda: print("Done!")
)

