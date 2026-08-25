#function = a block of code that is executed only when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
def hello(name,age): #function header
    print("Hello!" + " How are you, " + name + "?") #function body
    print("How are you, " + name + "?")   
    print("You are " + str(age) + " years old.")

my_name = "Laiba"
my_age = 25
hello(my_name, my_age) #calling the function
#hello("Alice", 30) #calling the function
#hello("Bob", 35) #calling the function again
#inside brackets we can pass arguments to the function

