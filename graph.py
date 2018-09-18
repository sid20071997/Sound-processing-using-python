import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess
from scipy.integrate import quad
import scipy.integrate as spint

y1=[0,5,20,25,36,40,45,50,57,60,65]
x1=[0,20,47,62,91,100,123,143,153,177,180]
y2=[0,10,20,30,45,52,61,65,71,81,90]
x=np.linspace(0,55,11)

plt.plot(x,y1)
plt.plot(x,y2)
plt.legend(["EDF-scheduling","RMS-scheduling"])
plt.xlabel('Number of processes')
plt.ylabel('Average waiting time')
plt.show()