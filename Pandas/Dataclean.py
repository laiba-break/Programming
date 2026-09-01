import pandas as pd

#Data Cleaning = the process of fixing/removing:
#incomplete,incorrect,or irrelevant data
# 75 percent of work done with Pands is data cleaning

df = pd.read_csv("pokemon.csv")

#1. Drop irrelevant columns
#df = df.drop(columns = ["Legendary", "No"])
#print(df)

# 2. Handle missing values
#if row missing a value we drop that entire row
#df = df.dropna(subset = ["Type2"])
#df = df.fillna({"Type2": "None"})
#print(df.to_string())

#3. Fix any inconsitent values

#df["Type1"] = df["Type1"].replace({"Grass": "GRASS" , "Fire" : "FIRE", "Water": "WATER"})

#clprint(df.to_string())


#4. Standardize text
#df ["Name"] = df["Name"].str.lower()

#print(df.to_string())

#5. Fix data types

#df["Legenday"]= df["Legendary"].astype(bool)
#print(df.to_string())

#6. Remove duplicate values
#print(df.to_string()) #duplicate enteries made

df = df.drop_duplicates()
print(df.to_string())