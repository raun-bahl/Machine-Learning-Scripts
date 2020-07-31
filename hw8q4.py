import numpy as np
import pandas as pd 
import math
import matplotlib.pyplot as plt

numbers = np.array(pd.read_csv('hw8.csv',header = None))

x1= numbers[:,:500]
x2 = numbers[:,500:1000]
theta = numbers[:,-1]



data_space = np.linspace(0,499,500)
K_ac = []

for i in range(len(data_space)):
	k2 = (1/(2*math.pi))*(math.sin(theta[i]) + math.cos(theta[i])* (math.pi - theta[i]))
	k = (math.sin(theta[i]) + (math.pi- theta[i])* math.cos(theta[i]))/2*math.pi
	K_ac.append(k2)


k_app = []
N = 800
for j in range(len(data_space)):
	s = 0
	for k in range(1,N):
		w = np.random.normal(0,1,500)
		s = s + (max(0,np.dot(w,x1[j,:])) * max(0,np.dot(w,x2[j,:])))
	k_app.append(s/N)


plt.plot(K_ac, theta, c = 'r', label = 'k_ac')
plt.scatter(k_app,theta, c = 'g', label = 'k_approx')
plt.xlabel('X')
plt.ylabel('Theta')
plt.title('Plot of the Arc-cosine kernel versus its equivalence')
plt.legend()
plt.show()