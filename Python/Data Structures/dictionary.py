# dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

capitals ={"USA": "Washington DC", "France": "Paris", "Germany": "Berlin"}
#print(capitals["India"])
print(capitals.get("India")) #returns None if key is not found
print(capitals.keys()) #returns all the keys in the dictionary
print(capitals.values()) #returns all the values in the dictionary
print(capitals.items()) #returns all the key-value pairs in the dictionary
capitals.update({"India": "New Delhi"}) #adds a new key-value pair to the dictionary    
print(capitals)
capitals.pop("Germany") #removes the key-value pair with the specified key
print(capitals)
capitals.clear() #removes all the key-value pairs from the dictionary