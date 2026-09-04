# initializing dictionary
test_dict = {'gfg' : {'a' : 4, 'b' : 5, 'c' : 8},
             'is' : {'a' : 8, 'c' : 10},
             'best' : {'c' : 19, 'b' : 10}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Nested Dictionary values summation
# Using loop + items() + values()
res = dict()
for sub in test_dict.values():
    for key, ele in sub.items():
        res[key] = ele + res.get(key, 0)

# printing result 
print("The summation dictionary is :" + str(res))