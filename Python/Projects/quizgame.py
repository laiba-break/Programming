#quiz game
#create a project where questions are presented and program cals final score
#radnomize questions and show which were answers incorrectly
#use lists, dictionaries, loops, functions, strings, conditional
import random

#function  to explain rules to user and introduce the game in general
def rules():
    print("Welcome to the Quiz Game")
    print("This game has a total of five questions. You are to attempt all of them")
    print("Each question carries one point and there is no negative marking.")
    print("You are required type in the correct answer.")
    print("At the end you will recieve your final score and answer to the questions you got wrong")

#after introducing the game now we will start with our main function
#i will store five questions string in a list and use while loop to keep it going 
#till it reaches length of the list use schfulle to randomize
 
def game():
    score = 0
    dict_1 =  {"Q1-Who created Python?": "Guido van Rossum",
                  "Q2- When was Python created?":"1991",
                   "Q3- Who created Linux?":"Linus Torvalds",
                   "Q4-Who created Microsoft":"Bill Gates",
                   "Q5.What does AI stand for?":"Artificial Intelligence"}
    i = 0  #starts from zero
    res= list(dict_1.items()) #randomizes the questions ans in dict
    #print(res)
    random.shuffle(res)
    question , answer = res[i]
    #print(question)
    #print(answer)

    #prints random question and answer
    dict_ans={}  #initalize empty dictionary 
    for question,answer in res:
       print(question)  #prints question
       answers = str(input("Please type your answer:")) #user types their answer
       if(answers == answer):
        score += 1
        print("You are right")
       else:
        print("You are wrong")
        dict_ans[question] = answer#stores wrong answer in dictionary
    i += 1

    print(dict_ans)
    print("Your Score is:" +str(score) + " out of 5")

rules()
game()







"""def game(score):
    questions = list (("Q1-Who created Python?",
                  "Q2- When was Python created?",
                   "Q3- Who created Linux?",
                   "Q4-Who created Microsoft",
                   "Q5.What does AI stand for?"))
    answer = list( ("Guido van Rossum", 
                "1991", 
                "Linus Torvalds", 
                "Bill Gates", 
               "Artificial Intelligence"))

    i = 0  #starts from zero
    j = 0 


    wrong_ans={}  #initalize empty dictionary 
#print(len(questions))
    while(i < len(questions) and (j < len(answer))):
        print(questions[i])  #prints question
        answers = str(input("Please type your answer:"))
        if (answers == answer[j]):
           print("You are right")
           score +=1
        else:
           print("You are wrong")
        i +=1   #increments it 
        j +=1
    print("Your Score is:" +str(score) + " out of 5")"""

#rules()
#game(0)






#each question will compared with answer given to it in a list also
#if right a plus one score given and next question asked
#if wrong no score given and next question asked
#the wrong answrs will be stored in a dictionary key question, value ans 
#final score will be incremented
#another function will be called for final quiz wind up





