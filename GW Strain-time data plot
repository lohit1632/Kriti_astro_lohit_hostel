import matplotlib.pyplot as plt
import numpy as np
!wget https://raw.githubusercontent.com/SAURABH-RAI1729/KRITIGW/main/GW150914_strain_data_final.txt
#open the data file in read mode, store each line in a list and close file
file = open('GW150914_strain_data_final.txt', 'r')
data = file.readlines()
file.close()

#collect the x and y values by splitting the lines, converting the strings to float and appending them to lists
time = np.array([])
strain = np.array([])

for line in data:
    x, y = map(float, line.split())
    time = np.append(time, x)
    strain = np.append(strain,y)

#plot using matplotlib
plt.plot(time, strain, '-')
plt.xlabel('Time')
plt.ylabel('Strain')
plt.title('Time-series plot of gravitational strain.')
plt.show()
