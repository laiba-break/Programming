#tuples =  a collection which is ordered and unchangeable used to group together related data

student = ("Bro", 21, "male")

print(student.count("Bro")) #how many times "Bro" appears in the tuple
print(student.index("male")) #tells the index of "male" in the tuple

for x in student:
   print(x)

if "Bro" in student:
   print("Bro is here!")


