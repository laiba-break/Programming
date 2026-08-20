#set is a collection that is unordered and unindexed

utensils = {"fork", "spoon", "knife"}

for utensil in utensils:
    print(utensil) 

utensils.add("napkin")
print(utensils)

utensils.remove("fork")
print(utensils)

#utensils.clear()
#print(utensils)

dishes = {"bowl", "plate", "cup", "knife"}
#utensils.update(dishes)
#print(utensils)
#dinner_table = utensils.union(dishes)
#print(dinner_table)
#dinner_table2 = utensils.difference(dishes)
#print(dinner_table2)
print(utensils.intersection(dishes))

