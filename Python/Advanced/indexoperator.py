#index operator is used to access the elements of a list, tuple, or string by their index. The index operator is represented by square brackets [] and is used to retrieve the value at a specific index in a sequence.

name = "bro Code!"
print(name[0]) #prints the first character of the string

#if(name[0].islower()):
 #   name = name.capitalize()
  #  print(name) #prints the string with the first character capitalized

first_name = name [0:3].upper() #slices the string from index 0 to 2 (3 is not included)
print(first_name) #prints "bro"
last_name = name[4:8].lower() #slices the string from index 4 to 7 (8 is not included)
print(last_name) #prints "code"

last_character = name[-1] #prints the last character of the string
print(last_character) #prints "!"