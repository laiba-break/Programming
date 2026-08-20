import os

path =r"C:\Users\LAIBA MEMON\Downloads\SKills_Laiba\Python\laiba.txt"
# the slash should be other direction

if os.path.exists(path):
    print("This exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is directory!")
else:
    print("Does not")


