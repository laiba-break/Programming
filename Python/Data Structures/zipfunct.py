#zip (*iterables) = aggregrate elements from two or more iterables (list,tuples,sets,etc)
#creates a zip object with paired elements in tuples for each element

username = ["Dude","Bro","Mister"]
password = ["password","abc123","guest"]

users = dict(zip(username,password))
 #print(type(users))

#for i in users:
 #   print(i)
for key,value in users.items():
    print(key+": "+value)

#----------------------------------------------#

login_date=["1-1-2021","1-2-2021","1-3-2021"]

users = zip(username,password,login_date)

for i in users:
    print(i)

    
