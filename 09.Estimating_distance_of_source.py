import numpy as np
from pycbc.waveform import get_td_waveform

# Function to estimate distance to source from waveform amplitude
def estimate_distance_from_waveform(chirp_mass, amplitude):
    k = 1.0

    # Calculate distance
    distance = np.sqrt(k / amplitude)
    return distance

# Function to generate waveform and estimate distance
def generate_waveform_and_estimate_distance(chirp_mass):
    # Generate time-domain waveform
    waveform, _ = get_td_waveform(approximant='SEOBNRv4_opt',
                                   mass1=chirp_mass, mass2=chirp_mass,
                                   delta_t=1.0/4096, f_lower=20)

    # Calculate peak amplitude of the waveform
    peak_amplitude = max(np.abs(waveform))

    # Estimate distance to source
    distance = estimate_distance_from_waveform(chirp_mass, peak_amplitude)
    return distance

# Example: Estimate distance for a chirp mass of 30 solar masses
chirp_mass = 26.6
estimated_distance = generate_waveform_and_estimate_distance(chirp_mass)
print("Estimated distance to source:", estimated_distance, "light years")
