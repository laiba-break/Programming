import os
import shutil
path = r"C:\Users\LAIBA MEMON\Downloads\SKills_Laiba\Programming\Python\text.txt"


try:
   #os.remove(path) #delete a fil
   os.rmdir(path) #delete an empty directory 
   shutil.remtree(path) #delete a directory comntaining files

except  FileNotFoundError:
    print("That file was not found")
except PermissionError:
   print("You do not have permission to delete that")
else:
    print(path +"was deleted")

