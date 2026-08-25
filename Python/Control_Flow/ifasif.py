#if statement = a block of code that will execute if condition is true 
age = int(input("Enter your age: "))

if age == 100:
    print("You are a centenarian")
elif age >= 20:
    print("You are eligible to vote")
elif age<5:
    print("You are a baby")
else:
    print("You are not eligible to vote")
