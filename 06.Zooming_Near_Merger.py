import numpy as np
import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform
from scipy.signal import find_peaks
# Function to generate and plot a time-domain waveform
def generate_and_plot_waveform(mass1, mass2):
    # Generate time-domain waveform
    waveform, _ = get_td_waveform(approximant='SEOBNRv4_opt',
                                   mass1=mass1, mass2=mass2,
                                   delta_t=1.0/4096, f_lower=20)
    peak_strain = max(np.abs(waveform))
    # Zoom in near the merger time
    plt.figure(figsize=(10, 5))
    plt.plot(waveform.sample_times, waveform, label=f'Mass1={mass1}, Mass2={mass2}')
    plt.xlabel('Time (s)')
    plt.ylabel('Strain')
    plt.title('Time-Domain Waveform (Zoomed In)')
    plt.xlim(waveform.sample_times[-700], waveform.sample_times[-1])
    plt.legend()
    plt.show()
# Generate and plot waveforms for different masses
generate_and_plot_waveform(36.2,29.1)
