d = {'a': 100, 'b': 200, 'c': 300}
res = sum(d.values())
print(res)

def stop():  #this is a function for stop
    #since it used again and again instead of copy pasting we call 
    #this is used to go main menu after each work is done
     while True:  #this keeps runnign until quit is entered
        answer = input("Please type quit to return to Main Menu:")
        if answer == "quit":
            break  #it breaks out of the code loop
##TO WASTE LESS TIME FOR CLI USE THIS STANDARD BELOW AND CHANGE
while True:
    choice = int(input("Select your choice:"))
    while choice ==1:
      print("It works")
      stop()
      break
    while choice ==2:
       print("It Works") 
       stop()
       break   
    while choice ==3:
       print("It works")
       stop()
       break
    while choice==4:
       print("it works")
       stop()
       break
    while choice==5:
        print("it works")
        stop()
        break
    if choice == 6:
        break