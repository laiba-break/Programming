name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
age += 1

print("Hello " + name + "! You are " + str(age) + " years old.")
print("Your height is " + str(height) + " cm.")

#you cannot use strings with integers so we have to convert age into string using str() function
