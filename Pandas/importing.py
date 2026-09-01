import pandas as pd

#learning to import csv and jason files using pandas
#data. csv and data.jason
#jason means java script object notation
df = pd.read_csv("pokemon.csv") #similiary u read_jason("") for jason file

#print(df) #prints trankated version first 5 and last 5 
# to print whole
print(df.to_string())

#some values werent present with NaN