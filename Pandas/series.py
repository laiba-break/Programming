#series continues
import pandas as pd

data = ["Bulbasaur","ivysaur","venusaur","Charmander","Charmeleon","Charizard"]


series  = pd.Series(data,index =[1,2,3,4,5,6])
print(series)