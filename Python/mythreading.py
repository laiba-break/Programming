#thread = a flow of execution. Like a seperate order of instructions.
#however each thread takes a turn running to achieve concurrency 
#GIL (Global intrepreter lock)
#allows only one thread to hold the control of the python intrepreter

#cpu bound = program/task spends most of its time waiting for internal events (CPU into
#use multiprocessing
#io bound = program/task spends most of its time waiting for external events (user input,web scraping)
#user input use mutlithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You have breakfast")

def drink_coffe():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You finish studying")

x = threading.Thread(target=eat_breakfast,args=())
x.start()
y = threading.Thread(target=drink_coffe,args=())
y.start()
z = threading.Thread(target=study(),args=())
z.start()

x.join() #main function has to wait for thread x to move on
y.join()
z.join()


#eat_breakfast()  #so we compelte these takss sequentially and we give sec
#rink_coffe()
#tudy()



print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())
#eg in quiz we can have one thread for input and one for count down
#so one is idle so its io bound


