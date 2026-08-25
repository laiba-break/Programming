#sort() method= used with lists 
# sort() function = used with iterables

student = ["Squidwerd", "Sandy", "Patrick", "Mr Krabs"]

student.sort()

for i in student:
    print(i)

    # works only with list 
    #sorts in alpbatical order

sorted_students = sorted(student)

for i in sorted_students:
    print(i)

    