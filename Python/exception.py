#exception = events detected during execution that intreupt the flow of a programming 

try:
    numerator = int(input("Enter a number to divide:"))
    demonitor = int(input("Enter a number to divide:"))
    result = numerator / demonitor
    print(result)
except ZeroDivisionError:
    print("Idiot")
except ValueError:
    print("number please")
except Exception:
    print("Wrong bro")
else:
    print(result)
finally:
    print("This will alwazs execute")
    