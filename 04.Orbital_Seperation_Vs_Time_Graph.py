import numpy as np
import matplotlib.pyplot as plt

# Function to calculate orbital separation as a function of time
def orbital_separation(t, r0, T_coalesce):
    return r0*(1-t/T_coalesce)**(1/4)

# Function to calculate strain amplitude as a function of time (simplified)
def strain_amplitude(t, amplitude_factor, coalescence_time):
    return amplitude_factor / (1 + np.exp(-(t - coalesce_time)))

# Set initial parameters
r0 = 1.0  # Initial orbital separation
T_coalesce = -(-0.5-coalesce_time)  # Coalescence time
amplitude_factor = strain[coalesce_time_index]#7.259311339647647e-19

# Generate time values
time_val = np.linspace(0, T_coalesce, 1000)

# Calculate orbital separation for each time value
orbital_separation_values = orbital_separation(time_val, r0, T_coalesce)

# Calculate strain amplitude for each time value (simplified)
strain_amplitude_values = strain_amplitude(time_val, amplitude_factor, T_coalesce)

# Plot the orbital separation and strain vs. time
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(time_val, orbital_separation_values, label='Orbital Separation')
plt.xlabel('Time')
plt.ylabel('Orbital Separation')
plt.title('Orbital Separation vs. Time')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(time_val, strain_amplitude_values, label='Strain Amplitude')
plt.xlabel('Time')
plt.ylabel('Strain Amplitude')
plt.title('Strain Amplitude vs. Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
