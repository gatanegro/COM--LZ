# Compute energy field tensions using gradients (force-like terms)

# Compute energy field gradients (tensions between nodes)
energy_gradient_x = np.gradient(energy_density, axis=0)  # Change in x-direction
energy_gradient_y = np.gradient(energy_density, axis=1)  # Change in y-direction

# Compute total tension field magnitude
tension_field = np.sqrt(energy_gradient_x**2 + energy_gradient_y**2)

# Compute the mean tension value (to see if forces are present across the system)
mean_tension = np.mean(tension_field)

# Visualize the tension field
plt.figure(figsize=(6, 6))
plt.imshow(tension_field, cmap="inferno", origin="lower")
plt.colorbar(label="Tension Magnitude")
plt.title("Tension Field in the Collatz Octave Model (COM)")
plt.show()

# Return computed mean tension value
mean_tension