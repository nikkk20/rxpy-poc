#Description
#This is a example program creating observables

from rx import of,operators as op

test = of(1,2,3,4)

subscriber = test.pipe(
    op.filter(lambda s: s%2 != 0),
    op.reduce(lambda acc,X: acc + X)
)
subscriber.subscribe(lambda x: print("Sum = {}".format(x)))

