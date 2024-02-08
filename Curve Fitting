from scipy.optimize import curve_fit
#Defining the exponential Model
def exp(x,a,b,c,d):
    return (a * (np.exp(b*x))) +c*x + d
def quadratic(t,a,b,c):
      return a * t**2 + b * t + c
inspiral_phase = -10
plt.step(time_peaks[inspiral_phase:], frequencies[inspiral_phase:], label='Step Function')
g = 6.67430*pow(10,-11)
c = 300000000
params,_ = curve_fit(exp, time_peaks[inspiral_phase:], frequencies[inspiral_phase:])
fitted_curve = exp(time_peaks[inspiral_phase:], *params)
plt.plot(time_peaks[inspiral_phase:],fitted_curve)
plt.xlabel('Time')
plt.ylabel('Frequency (Hz)')
plt.title("Frequency Vs Time with Curve Fit")
plt.legend()
plt.grid()
plt.show()
