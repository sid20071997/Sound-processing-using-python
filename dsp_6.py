import soundfile as sf
import numpy as np
from scipy import signal
from sympy import apart
import matplotlib.pyplot as plt




input_signal , fs = sf.read('Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_freq = 4000.0

Wn = 2*cutoff_freq/sampl_freq

b,a = signal.butter(order,Wn,'low')

output_signal = signal.filtfilt(b,a,input_signal)

b = b[::-1]
a = a[::-1]


r, p,k = signal.residue(b,a)

n = np.linspace(0,30)
h = []
for i in range(0,30):
    s = 0
    for j in range(0,order):
        s = s - r[j]/(p[j]**(i+1))
    if (i==0):
        s=s+k[0]
    h.append(np.real(s))

y1=np.convolve(input_signal,h)
y = []
for i in range(0,input_signal.size):
     s = 0
     for j in range(0,30):
         if(i-j>=0):
         	s = s + input_signal[i-j]*h[j]
         else:
         	break
     y.append(s)

print(y1[0:10])
print(output_signal[0:10])
print (input_signal[0:10])
print (h[0:10])
print ("hi")
plt.stem(range(30),h)
plt.show()

sf.write('Sound_with_reducedNoise6.wav',y,fs)