import pandas as pd

#series  = a pandas 1d labelled array that can hold any data type think of it like a single column in a spreadsheet (1D)

data = [100, 102, 104,200,202]
data2 = ["A","B","c"]

series = pd.Series(data, index=["a","b","c","d","e"]) #we changed our labels can even make a string
series2 = pd.Series(data2)

series.loc["c"] = 200 #we changed the value
# u can also print location postion
print(series.iloc[0]) #location by label

print(series.loc["c"]) #gives data type and we can also change dattype
#.loc returns location that label is 
print(series2)
#we can also use booleans
#the default number it starts at is zero

#now we will filter by values
print(series[series >=200]) 

#python dictionary to count the calories we have 
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)
print(series)
series.loc["Day 1"] += 500
print(series.loc["Day 3"])
print(series.loc["Day 1"])
print(series[series <= 2000]) 
#its like a single 
