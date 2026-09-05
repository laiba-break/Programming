#expense tracker 
#Create a command-line program where a user can add expenses, view their expenses, 
# calculate total spending, and categorize spending.
#Example:
#1. Add expense
#2. View expenses
#3. Total spent
#4. Spending by category
#5. Exit
#Use:lists,dictionaries,functions,loops,conditions ,datetime ,file handling (.txt or .csv) ,possibly csv 
#Practice goal: Build your first CRUD-style application and learn to persist data.
import json  #import json library to work with file handling
#the purpose of file handling in this program
#this helps saves data and when program is off that data will be stored in a file
#this data can also ne edited and deleted 
#json is used for storing and exchanging data
import os #built in module that helps interact with creating files etc
from time import *


expense_log ={}
 #initalized an empty dict of expenses
#this dictionary will store the three spending categories as key and their values

def stop():  #this is a function for stop
    #since it used again and again instead of copy pasting we call 
    #this is used to go main menu after each work is done
     while True:  #this keeps runnign until quit is entered
        answer = input("Please type quit to return to Main Menu:")
        if answer == "quit":
            break  #it breaks out of the code loop

def save_expenses():  #this is a seperate fucnction created to save expenses added
    #this will be used in the add expenses loop
    with open("delexpense.txt", "w") as file: # we write in the file
        json.dump(expense_log, file) #.dump is used to write into a file
    
def load_expenses(): #function for loading the data on to file 
    if os.path.exists("delexpense.txt"):
        try:
            with open("delexpense.txt", "r") as file:
                return json.load(file) #this may sometimes raise a erro
        except json.JSONDecodeError:
            return {}  #if it does raise it then it wont crash the system
    return {}

def categ():
      print("Select your category")
      print("1. Rent")
      print("2. Grocery")
      print("3. Health Insurance")


expense_log = load_expenses()
while True:
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total spent")
    print("4. Spending by category")
    print("5. Exit")
    choice = input("Select an option number:")


    while choice == "1":
        categ()
        n = int(input("Enter the total number of entries: "))
        #TEMPORARY FOR TESTING ONLY
        #t = "06:Sept:2026"
        t= strftime("%d:%b:%Y")
        for _ in range(n):
            category = input("Enter category: ")
            value = float(input("Enter value: "))
            expense_log.setdefault(t, {}).setdefault(category, []).append(value)
        save_expenses()
        stop()
        break ##laiba    
    while choice == "2":
        load_expenses()
        print("Expenses Entered are:", expense_log)
        stop()
        break
    
    while choice == "3":
       # total = sum(expense_log.values()) this only we for one dict
       # for nexted loop is required to each values
       # date to category to value
       total =0
       for date_dict in expense_log.values():
           for value_list in date_dict.values():      # loop through each category's list, within that date
               total += sum(value_list)                # add up that list's numbers, accumulate into total
       print("Total Expenses are:", total)
       stop()
       break

    while choice == "4":
        categ()
        t= strftime("%d:%b:%Y")
        n = int(input("Enter your choice:"))
        if (n ==1):
            print(expense_log.get(t,{}).get("Rent")) #nested dictionary to get value
        elif (n==2):
            print(expense_log.get(t,{}).get("Grocery"))
        elif (n==3):
            print(expense_log.get(t,{}).get("Health Insurance"))
        else:
            print("Wrong Choice")
        stop()
        break

    if choice == "5":
        break
