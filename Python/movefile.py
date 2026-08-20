import os

source = "file.txt"
destination = r"C:\Users\LAIBA MEMON\Downloads\SKills_Laiba\Python\file.txt"

try:
    if os.path.exists(destination):
        print("There is a file")               
    else:
         os.replace(source,destination)
         print("was moved")
       
except FileNotFoundError:
    print(source + "was not found")

