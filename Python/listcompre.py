#list comprehensions = a way to create a list with less syntax
# can micmic certain lamda functions, easier to read
# list= [expression for items in iterable]

squares = []     #create a empty list
for i in range(1,11): #create for loop
    squares.append(i * i)  #define what each loop iteration should do
print(squares)

squares =  [i * i for i in range(1,11)]
print(squares)

#this took lesser code to tell how to fill list
students = [100,90,80,70,60,50,40,30,9]
passed_students = list(filter(lambda x: x>= 60, students))

print(passed_students)

passed_students= [i for i in students if i>= 60]
print(passed_students)

#make list with less snytax


