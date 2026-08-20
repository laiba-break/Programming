# keyword arguments are used to pass arguments to a function by explicitly stating which parameter the value should be assigned to. 
# This allows for more flexibility in the order of arguments and can improve code readability.

def greet(name, age):
    print("Hello,"+ name +"  You are " + str(age) + " years old.")

# Calling the function with keyword arguments
greet(name="Alice", age=30)
greet(age=25, name="Bob")   