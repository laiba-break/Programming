import matplotlib.pyplot as plt
import numpy as np

#print(matplotlib.__version__)

x = np.array([2023,2024,2025,2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17,23,38,5])
y3 = np.array([20,25,30,35])

line_style = dict(marker = ".",
         markersize = 20,
         markerfacecolor = "Red",
         markeredgecolor = "Cyan",
         linestyle = "dashed",
         linewidth = 4)


plt.plot(x,y1, color = "Green", **line_style)  
plt.plot(x,y2, color= "Red",** line_style)
plt.plot(x,y3, color= "Blue", ** line_style)



#can also use hex value
#markers on python wesbite list #u can add one and they will automitcally give 0.5 increments
plt.show()



