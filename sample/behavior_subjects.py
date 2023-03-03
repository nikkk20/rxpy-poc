#Description
#This is a example program showing the use of behavior subjects.

from rx.subject import BehaviorSubject
 
#Creating the behavior subject
behavior_subject = BehaviorSubject("hi")
behavior_subject.on_next("hello")

#First subscriber
behavior_subject.subscribe(
    lambda x: print("Got - 1 {}".format(x))
    
)
behavior_subject.on_next("Hello testting")

#second subscriber
behavior_subject.subscribe(
    on_next=lambda x: print("Got - 2 {}".format(x))
    
)