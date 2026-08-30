import random

#we imported the library random
#objective is that computer chooses a random number and 
# #user keeps guessing till they are right
# computer choose a random number from 0 to 10
# we will schuffle the list of numbers
#we will ask input from user to guess the number
#if users guesses the right number then it displays u guessed right
#if user guesses wrong then it aks user again and again till he gets it right
#we will use comaprison operators to check 
# to keep that ig going we use while loop 
# we will create one function for computer
# we will create on fucntion for user
#after he gueesses right it will show a counter this counter shows how many tries
#how many wrong and how many right
computer_nm = random.choice(range(0,10))
#def computer(value):
 #       value=computer_nm
  #      print("Computer chose the number: "+ str(computer_nm))
   #     return int(computer_nm)

def user(computer_num):
    attempt =0
    loss = 0
    winner = 0
    user_number = input("Enter your guess number between 0 and 10:") #this will return str
    attempt +=1
    if int(user_number) == computer_nm: 
        winner = 1
        print("Congratulations, you guessed right")
        print("You Won")
        print("Computer chose the number: "+ str(computer_num))
        print("You recently chose: " +str(user_number))
        print("You attemped: "+ str(attempt))
        print("You lost: " + str(loss))
        print("You won: " +str(winner))
    else:
        loss+=1
        while int(user_number) != computer_num:
            keep_going =input("Would you like to keep trying?(yes/no):")
            if keep_going.lower() == "yes" :
                while int(user_number) != computer_num and attempt<=10:
                   attempt+=1
                   loss +=1
                   print("This is attempt number: " + str(attempt))
                   user_number = input("Enter your guess number between 0 and 10 again:")
                   if int(user_number) == computer_num:
                        winner +=1
                        print("Congratulations, you guessed right")
                        print("You Won")
                        print("Computer chose the number: "+ str(computer_num))
                        print("You recently chose: " +str(user_number))
                        print("Attempts: "+str(attempt))
                        print("Loss: " +str(loss))
                        print ("Winner: " +str(winner))
                        break
                   else:
                       loss +=1
                       print("This was attempt number: " + str(attempt))
                       print("You Lost:" +str(loss))
                       break #will ask you again do you want to play
                       
            else:
                 print( "Game has come to an end")
                 print("You lost") 
                 print("Computer chose the number: "+ str(computer_num))
                 print("You recently chose:" +str(user_number))
                 print("Attempts: "+str(attempt))
                 print("Loss: " +str(loss))
                 print ("Winner: " +str(winner))
                 break





#computer(value = computer_nm)
user(computer_num=computer_nm)


    

