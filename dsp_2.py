from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
import scipy
import scipy.stats as sp	
import subprocess

def sinc(f):
	return np.sin(np.pi*f)/(np.pi*f)

simlen=100000
p=100
f=np.linspace(-4*np.pi,4*np.pi,simlen)

vec_sinc=scipy.vectorize(sinc)
plt.plot(f,vec_sinc(f))
plt.grid()
plt.show()
