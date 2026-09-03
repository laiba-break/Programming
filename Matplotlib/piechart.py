import matplotlib.pyplot as plt
import numpy as np

#Bar Chart = Circular chart divided into slices to show percentages of the total 
#good for visualizing distributions among categories 

categories = ["Feshmen", "Somphmores","Juniors","Seniors"]
values = np.array([300,250,275, 225])
colors=["red","yellow","blue","green"]


plt.pie(values,labels = categories,
        autopct = "%1.1f%%",
        colors= colors,
        explode =[0, 0, 0, 0.1],
        shadow = True,
        startangle = 90)

plt.title("Bro Code College")
plt.show()
