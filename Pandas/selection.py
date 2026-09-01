import pandas as pd

df = pd.read_csv("pokemon.csv",index_col = "Name")

#SELECTION BY COLUMN

#print(df["Name"].to_string())
#print(df["Height"].to_string())

#print(df[["Name","Height","Weight"]].to_string())

#SELECTION BY ROWS
#print(df.loc[1])
#print(df.loc["Pikachu"])
#print(df.loc["Charizard": "Blastoise", ["Height","Weight"]])
#print(df.iloc[0:11:2, 0:3]) #first ten rows and first three columns 

pokemon = input ("Enter a pokemon name:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")



