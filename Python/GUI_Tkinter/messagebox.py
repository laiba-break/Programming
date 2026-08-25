from tkinter import *
from tkinter import messagebox #import message box library

def click():
   # messagebox.showinfo(title= "WARNING", message="U HAVE A VIRUS")
   # while(True)
 #  messagebox.showerror(title="Error",message="something went wrong")
    #if messagebox.askokcancel(title= "okay cancel",message= "Do u want to do the thing"):
     #  print("u did the thing")
    #else:
     #   print("u did not")
    # if messagebox.askyesno(title="ask yes or no", message = "Do u like cake?"):
       #  print("i like cake too")
    # else:
      #    print("why do not like cake")  #this is message box asking for yes or no
     # answer= messagebox.askquestion(title="ask question",message="do u like pie")
     # if (answer == 'yes'):
     #      print("I like pie too")
    # else:
      #      print("why nott")
      answer = print(messagebox.askyesnocancel(title = " yes no cancel",message= "do u like to code",icon="warning"))
      if (answer == True):
          print("great")
      elif(answer== False):
          print("Then why are u watching a video on coding")
      else:
         print("u doged it")

window = Tk()
button = Button(window,command=click,text= "click me")
button.pack()
window.mainloop()