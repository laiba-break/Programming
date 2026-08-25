# kwargs = parameter that will pack all arguments into a dictionary 
#useful so that function will accept a varying amount of keyword argument 

def hello(**kwargs):
    print("Hello " + kwargs["first"] +" " +kwargs["last"])
    for key, value in kwargs.items():
        print(value,end=" ")
hello(title="Mr ", first= "Bro", middle="Dude",last="Code")
