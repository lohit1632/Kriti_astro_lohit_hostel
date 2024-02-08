import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

#reading data
file = open('GW150914_strain_data_final.txt', 'r')
data = file.readlines()
file.close()

time = np.array([])
strain = np.array([])

for line in data:
    x, y = map(float, line.split())
    time = np.append(time, x)
    strain = np.append(strain, y)

#collecting the indexes of the peak strains in 'peeks'
peaks, _ = find_peaks(strain)
time_x=[]
for i in range(0,len(peaks)-1):
   time_x.append(time[peaks[i]])
time_diff=[]
for i in range(0,len(time_x)-1):
  time_diff.append(time_x[i+1]-time_x[i])
time_peaks = time[peaks]

# #using diff to collect time intervals between consecutive peaks
intervals = np.diff(time[peaks])

# frequency = 1/timePeriod
frequencies = 1/intervals
frequency=[]
for i in range(0,len(time_diff)):
  frequency.append(1/time_diff[i])
plt.step(time[peaks][1:],frequencies)
#starting from index 1 because number of intervals one less than number of peaks
plt.xlabel('Time')
plt.ylabel('Frequency (Hz)')
plt.title("Frequency Vs Time")
plt.grid()
plt.show()
