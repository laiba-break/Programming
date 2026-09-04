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
expenses = {} #initalized an empty dict of expenses
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

def tim():
    t= strftime("%d:%b:%Y")
    expense_log ={t:expenses}
   # print(expense_log)

expenses = load_expenses()
while True:
    print("Program is running...")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total spent")
    print("4. Spending by category")
    print("5. Update Expenses")
    print("6. Delete Expenses")
    print("7. Exit")
    choice = input("Select an option number:")

    while choice == "1":
        categ()
        n = int(input("Enter the total number of entries: "))
        t= strftime("%d:%b:%Y")
        expense_log ={t:expenses}
        for _ in range(n):
            category = input("Enter category: ")
            value = float(input("Enter value: "))
            expenses.setdefault(category, []).append(value) #this helps update value with key
            save_expenses()
        stop()
        break ##laiba

    while choice == "2":
        
        print("Expenses Entered are:", expense_log)
        stop()
        break
    while choice == "3":
        res = dict()
        for sub in expense_log.values():
            for key, ele in sub.items():
                res[key] = ele + res.get(key,0)
        total = str(res)
        print("Total Expenses are:", total)
        stop()
        break

    while choice == "4":
        categ()
        n = int(input("Enter your choice:"))
        if (n ==1):
            print(expense_log["Rent"])
        elif (n==2):
            print(expense_log ["Grocery"])
        elif (n==3):
            print(expense_log["Health Insurance"])
        else:
            print("Wrong Choice")
        stop()
        break

    while choice == "5":
        print("Expenses Entered are:", expenses)
        stop()
        break
    
    while choice == "6":
        print("Expenses Entered are:", expenses)
        stop()
        break
    
    if choice == "7":
        break
