import numpy as np
import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform

# Function to generate and plot a time-domain waveform using chirp mass
def generate_and_plot_waveform(chirp_mass):
    # Assume symmetric mass ratio for simplicity (equal masses)
    mass_ratio = 36.2/29.1
    mass1 = (chirp_mass*(mass_ratio+1)**(0.2))/(mass_ratio**(0.6))
    mass2 = mass1*(mass_ratio)
    # Generate time-domain waveform
    waveform, _ = get_td_waveform(approximant='SEOBNRv4_opt',mass1=mass1, mass2=mass2,delta_t=1.0/4096, f_lower=20)

    # Plot the waveform
    plt.figure(figsize=(12, 6))
    plt.plot(waveform.sample_times, waveform, label=f'Chirp Mass={chirp_mass}')
    plt.xlabel('Time (s)')
    plt.ylabel('Strain')
    plt.title('Time-Domain Waveform')
    plt.legend()
    plt.show()
# Generate and plot waveforms for different chirp masses
for i in range(20,41,5):
  generate_and_plot_waveform(i)



