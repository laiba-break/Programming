#logical operators (and,or and not ) is used to check if two or more conditonal statements are true or false

temp = int(input("Enter the temperature in degree Celsius: "))
if temp>=0 and temp<=30:
    print("The temperature is good today")
    print("Go outside")
#and both conditions must be true for the whole statement to be true
elif temp<0 or temp>30:
    print("The temperature is bad today")
    print("Stay inside")
#or only one condition must be true for the whole statement to be true
#not operator is used to reverse the result, returns False if the result is true
elif not(temp>=0 and temp<=30):
    print("The temperature is bad today")
    print("Stay inside")
