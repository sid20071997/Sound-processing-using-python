import soundfile as sf
from scipy import signal
input_signal,fs=sf.read('Sound_Noise.wav')

sampl_freq=fs
order=4
cutoff_freq=8000.0
Wn=2*cutoff_freq/sampl_freq
b,a=signal.butter(order,Wn,'low')
print(b)
print(a)
output_signal=[]
print(a.shape)
#print(input_signal)
output_signal.append(b[0]*input_signal[0]/a[0])
for i in range (1,input_signal.size):
	p=0
	q=0
	for j in range (0,5):
		if(i-j>=0):
			p+=b[j]*input_signal[i-j]
		else:
			break
	j=1
	while(j<=4):
		if(i-j>=0):
			q+=a[j]*output_signal[i-j]
		j=j+1
	output_signal.append((p-q)/a[0])	
sf.write('Sound_with_ReducedNoise.wav',output_signal,fs)
print (sampl_freq)