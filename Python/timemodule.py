import time

#epoch = a date and time from which a computer measures system time
#epoch = when ur computer thinks time began (ref point)
#print(time.ctime(10000000))

#time in second then make it readbla like full date

#print(time.time()) #returns seconds since epoch

#print(time.ctime(time.time())) #to get current date and time

#time_obj = time.localtime()
#print(time_obj)
#to cover time obj to readbale format we use below
#local_time = time.strftime("%B %d %Y %H %M: %S", time_obj)
#directives were this can be found online
#print(local_time)
#time_obj= time.gmtime()
#for function below we pass a string as date
time_string = "20 April,2021"
time_obect = time.strptime(time_string,"%d %B,%Y")
print(time_obect)

#(year,moth,day,hours,minutes,secs, #day of the week,#day of the year,dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

##(year,moth,day,hours,minutes,secs, #day of the week,#day of the year,dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
