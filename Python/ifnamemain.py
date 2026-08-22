#if __name__ == "__main__"
# why tho
#1. module can be run as standalone program
#2. module can be imported and used by other modules

#Python intrepreter sets "special variables" one of which is __name__
# then python will execute the code within __main__

#import moduletwo 

#print(__name__)
#print(moduletwo.__name__)

def hello():
    print("hello")

if __name__ == "__main__":
    print("running this module directly")

else:
    print("running other module indirectly")

