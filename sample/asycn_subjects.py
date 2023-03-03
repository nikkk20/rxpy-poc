#Description
#This is a example program showing the use of asyn subjects.

 

from rx.subject import AsyncSubject

#Creating a AsyncSubject
Async_Subject = AsyncSubject()

#Creating the first Subscriber
Async_Subject.subscribe(
    on_next= lambda x : print("Got 1 - {}".format(x))
)

#Passing values to the Subject
Async_Subject.on_next(1)
Async_Subject.on_next(2)
#Async_Subject.on_completed()

#Creating the Second Subscriber
Async_Subject.subscribe(
    lambda x : print("Got 2 - {}".format(x))
)
Async_Subject.on_next(3)
