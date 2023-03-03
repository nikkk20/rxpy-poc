
#Description
#This is a example program showing the use of replay subjects.

from rx.subject import ReplaySubject
#creating replay subject
Replay_Subject = ReplaySubject(2)
Replay_Subject.on_next("first")

#first subscriber
Replay_Subject.subscribe(
    on_next=lambda x : print("Got 1- {}".format(x))
)
Replay_Subject.on_next("Hello")
Replay_Subject.on_next("hi")

#second subscriber
Replay_Subject.subscribe(
    on_next=lambda x : print("Got 2- {}".format(x))
)
Replay_Subject.on_next("Hiii")
Replay_Subject.on_next("Hioi")
