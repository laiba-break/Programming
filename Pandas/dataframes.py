import pandas as pd

#Data Frame =  a tabular data sctructure with rows and columns. (2D) similiar to excel spreasheet

data = {"Name": ["Spongebob","Patrick","Squidward"] , 
        "Age": [30,35,50]
        }
df = pd.DataFrame(data,index = ["Employee 1", "Employee 2", "Employee 3"])

print(df.loc["Employee 1"]) #location by object
print(df.iloc[2])

#Add a mew column
#this how you add a new sc
df["Job"] = ["Cook", "N/A","Cashier"]


# add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
                        {"Name": "Eugene", "Age": 60, "Job": "Manager"}],
                       index = ["Employee 4", "Employee 5"])

df = pd.concat([df,new_row])

print(df)





