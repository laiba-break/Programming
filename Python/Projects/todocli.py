#creating a to do list cli interface
#cli is command line interface
#trying to make a terminal application where u can add tasks, view tasks
#complete tasks and delete task and exit them
# use lists, dictionaries, loops, CRUD logic, input validation
#save the tasks to a file so they remin even after program closed
#program strcutre is imp
#create a program where users can can add tasks, view tasks, mark tasks as compelted
#delete tasks and save tasks #load tasks when program starts 
#list- dictionaries, functions,loops, conditions, file handling
#Bonus:give each task an ID
import json
import time 
def stop():  #this is a function for stop
    #since it used again and again instead of copy pasting we call 
    #this is used to go main menu after each work is done
     while True:  #this keeps runnign until quit is entered
        answer = input("Please type quit to return to Main Menu:")
        if answer == "quit":
            break  #it breaks out of the code loop

tasks = []
print("LAIBA'S TO DO LIST CLI")

print("1. Add Task")

print("2. View Task")

print("3. Mark Task As Completed")

print("4. Delete Task")

print("5. Save Task")

print("6. Exit")

while True:
    choice = int(input("Select your choice:"))
    while choice ==1:
      str(input("Add Your Task:"))
      n = int(input("Enter the total number of entries: "))
      for _ in range(n):
        task[0]
      stop()
      break
    while choice ==2:
       print("It Works") 
       stop()
       break   
    while choice ==3:
       print("It works")
       stop()
       break
    while choice==4:
       print("it works")
       stop()
       break
    while choice==5:
        print("it works")
        stop()
        break
    if choice == 6:
        break