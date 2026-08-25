#lamda function = function written in 1 line using lamda keyword
#accepts any number of arguments, but only has one expression
#think of it as shortcut
#useuful if needed for a short period of time,throw only

#lamda parameters: expression

#def double(x):
 #   return x*2 
#print(double(5))

double = lambda x:x *2
multiply = lambda x, y: x*y
print(multiply(5,4))
add = lambda x,y,z : x+y+z
full_name= lambda first_name, last_name: first_name + " "+ last_name
print(double(5))
print(full_name("Bro","Code"))
age_check = lambda age: True if age>=18 else False
print(age_check(18))


