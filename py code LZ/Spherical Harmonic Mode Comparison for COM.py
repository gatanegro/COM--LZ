from scipy.special import sph_harm

# Define spherical harmonic parameters
theta = np.linspace(0, np.pi, grid_size)  # Polar angle
phi = np.linspace(0, 2 * np.pi, grid_size)  # Azimuthal angle
Theta, Phi = np.meshgrid(theta, phi)

# Compute the first-order spherical harmonic Y(l=3, m=2) as an example
Y_lm = sph_harm(2, 3, Phi, Theta).real  # Real part of the function

# Convert spherical coordinates to Cartesian for visualization
X_sph = np.sin(Theta) * np.cos(Phi)
Y_sph = np.sin(Theta) * np.sin(Phi)
Z_sph = np.cos(Theta)

# Plot the spherical harmonic wave mode
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_sph, Y_sph, Z_sph, facecolors=plt.cm.viridis(Y_lm), edgecolor="k")

ax.set_xlabel("X-axis (Spherical)")
ax.set_ylabel("Y-axis (Harmonic Mode)")
ax.set_zlabel("Z-axis (Energy Field)")
ax.set_title("Spherical Harmonic Mode Comparison for COM")

plt.show()