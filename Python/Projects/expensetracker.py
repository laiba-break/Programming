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
expenses = {}

def stop():
    while True:
        answer = input("Please type quit:")
        if answer == "quit":
            break

while True:
    print("Program is running...")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Total spent")
    print("4. Spending by category")
    print("5. Exit")
    choice = int(input("Select an option number:"))

    while choice == 1:
        print("Select your category")
        print("1. Rent")
        print("2. Grocery")
        print("3. Health Insurance")
        n = int(input("Enter the total number of entries: "))
        for _ in range(n):
            category = input("Enter category: ")
            value = float(input("Enter value: "))
            expenses[category] = value
        stop()
        break

    while choice == 2:
        print("Expenses Entered are:", expenses)
        stop()
        break

    while choice == 4:
        total = sum(expenses.values())
        print("Total Expenses are:", total)
        stop()
        break

    if choice == 5:
        break