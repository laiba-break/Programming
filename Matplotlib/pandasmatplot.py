import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("pokemon.csv")
type_count= df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index,type_count.values,color="lightblue",
         edgecolor = "black")

plt.title("# of Pokemon by Promary Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()

plt.show()

