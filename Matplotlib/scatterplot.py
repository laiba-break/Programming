import matplotlib.pyplot as plt
import numpy as np

#scatter plot = shows the relationship btw two variables 
#helps to identify a correlation (+,-,None)
#Examples: Study hours vs Test scores

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7,8])  #hours stuided 
y1 = np.array([55,60,65,62,68,70,75,78,82,85,87]) #grades 

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8,8])  #hours stuided 
y2 = np.array([55,58,65,70,72,78,83,78,88,92,95]) #grades 


plt.scatter(x1,y1,color = "skyblue",
            alpha = 0.5,
            s = 200,
            label= "Class A") #alpha is tranpsarency


plt.scatter(x2,y2,color = "red",
            alpha = 0.5,
            s = 200,
            label = "Class B") #alpha is tranpsarency

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend()

plt.show()

