import numpy as np
import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform
from scipy.optimize import curve_fit

# Function to generate and plot a time-domain waveform using chirp mass
def generate_and_plot_waveform(chirp_mass):
    # Assume symmetric mass ratio for simplicity (equal masses)
    mass_ratio = 36.2 / 29.1
    mass1 = (chirp_mass * (mass_ratio + 1) ** (0.2)) / (mass_ratio ** (0.6))
    mass2 = mass1 * (mass_ratio)
    waveform, _ = get_td_waveform(approximant='SEOBNRv4_opt', mass1=mass1, mass2=mass2, delta_t=1.0 / 4096, f_lower=20)
    peak_strain = max(np.abs(waveform))
    return peak_strain

def linear(x, a, b):
    return x * a + b

xpoints = np.array(list(range(20, 41)))
ypoints = np.array([generate_and_plot_waveform(i) for i in xpoints])
arr = np.array([strain[coalesce_time_index] for _ in xpoints])
params2, _ = curve_fit(linear, xpoints, ypoints)
fitted_curve2 = linear(xpoints, *params2)
x_coordinate=((strain[coalesce_time_index]-params2[1])/params2[0])
plt.axvline(x=x_coordinate, color='red', linestyle='--', label='Chirp Mass')
plt.plot(xpoints, fitted_curve2, "y", label='Fitted Curve')
plt.scatter(xpoints, ypoints, label='Peak Strain')
plt.plot(xpoints, arr, '-r', label='Peak Strain of our event')
plt.title('Peak strain vs chirp mass')
plt.ylabel('Peak_strain')
plt.xlabel('chirp_mass(solar_mass)')
plt.legend()
plt.grid()
plt.show()
print("Better estimated Chirp Mass - "+str(x_coordinate))
