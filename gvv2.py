import numpy as np
import mpmath as mp
import scipy
import scipy.stats as sp
import matplotlib.pyplot as plt
import subprocess

simlen=100000
n=np.random.normal(0,1,simlen)

mean =np.sum(n)/simlen

print (mean)

var=np.sum(np.square(n-mean*np.ones((1,simlen))))/simlen

print (var)