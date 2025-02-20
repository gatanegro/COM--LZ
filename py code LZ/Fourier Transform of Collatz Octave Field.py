from scipy.fft import fft, fftfreq

# Define the wave energy values in the COM system
wave_samples = [energy_values[n] for n in nodes]  # Extract energy values from graph nodes
num_samples = len(wave_samples)

# Perform Fourier Transform
freqs = fftfreq(num_samples, d=1)  # Frequency bins
fourier_transform = fft(wave_samples)  # Compute FFT

# Plot the Fourier Transform spectrum
plt.figure(figsize=(8, 4))
plt.plot(freqs[:num_samples//2], np.abs(fourier_transform[:num_samples//2]), 'o-', label="Frequency Spectrum")
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title("Fourier Transform of Collatz Octave Field")
plt.legend()
plt.grid(True)
plt.show()