#daemon thread  = a thread that runs in background, not important for program
#to run ur program will not wait for daemon threads to complete before exisiting
#non_daemon threads cannotnormally be killed, stay until task is complete. 
#ex.background tasks, garbage collectiion, waiting for input
#long running process

import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:",count , "seconds")

x= threading.Thread(target=timer,daemon=True)
x.start()

answer = input("do u wish to exit")