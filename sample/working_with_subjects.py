#Description
#This is a example program showing the use of subjects.


from rx.subject import Subject

subject_test = Subject()

    
subject_test.subscribe(
    on_next = lambda x: print("Got 1 : {0}".format(x)),
    on_error= lambda x: print("There is an error in 1: {}".format(x))
)

 

subject_test.subscribe(
    on_next= lambda x: print("Got 2 - {}".format(x)),
    on_error= lambda x: print("There is an error in 2: {}".format(x))
)
subject_test.on_next("A")


subject_test.on_next("B")
subject_test.on_error(Exception("There is an error"))


