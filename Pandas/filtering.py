import pandas as pd

df = pd.read_csv("pokemon.csv")

#tall_pokemon = df[df["Height"] >=2]
#print(tall_pokemon)

#heavy_pokemon =df[df["Weight"] >100]
#print(heavy_pokemon)

#leng_pokemon = df[df["Legendary"] == True]
#print(leng_pokemon)

water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)

ff_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"]=="Flying")]
print(ff_pokemon)