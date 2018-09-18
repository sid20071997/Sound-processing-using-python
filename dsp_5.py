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
i=0
for i in range(0,40):
    s = 0
    for j in range(0,order):
        s = s - r[j]/(p[j]**(i+1))
    if (i==0):
        s=s+k[0]
    h.append(np.real(s))
for i in range (40,len(input_signal)+1):
	h.append(0)

H=np.fft.rfft(h)
X=np.fft.rfft(input_signal)
Y=H*X
y1=np.real(np.fft.irfft(Y))
print(output_signal[0:10])
print(y1[0:10])
