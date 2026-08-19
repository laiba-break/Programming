#slicing = create a substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]
name = "Bro Code"
first_name = name[:3] #start index is included and end index is excluded
last_name = name[4:] #start index is included and end index is excluded
print(first_name)
print(last_name)
funky_name = name[0:8:2]     #start index is included and end index is excluded
reverse_name = name[::-1] #reversing the string
print(funky_name)
print(reverse_name)

website= "http://www.google.com"
website2= "http://www.youtube.com"
slice = slice (7, -4) #start index is included and end index is excluded
print(website[slice])
print(website2[slice])
