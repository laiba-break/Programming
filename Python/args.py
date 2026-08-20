# args = parameter that will pack all arguments into a tuple
#useful so that a function can accept a varying amount of arguments
# good when u have many arguments 

def add(*args): #u can name it sth else too not args 
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))
