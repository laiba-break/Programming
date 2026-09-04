

students = [("Squidward", "F", 60),
            ("Sandy", "A",33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20), 
            ("Mr Krabs", "C", 78)]

grade = lambda grades: grades[1] #we define that grades are the second col
students.sort(key=grade)

for i in students:
    print(i)
#this sorts them according to their grade and so you can change
