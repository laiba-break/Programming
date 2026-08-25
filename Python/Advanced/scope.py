# scope = the region that a veriable is recognized 
# A variable is only available from inside the region it is created 
# A global and locally scoped versions of a variable can be created 
name = "Bro"  #global variable inside and outside the function

def display_name():
    name = "Code"  #local scope (available only inside this function)
    print(name)

display_name()
print(name)

#python follows LEGB local.enclosed, global, built in