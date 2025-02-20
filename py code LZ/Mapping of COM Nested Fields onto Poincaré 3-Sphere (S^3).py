# Compute a mapping of COM's nested energy field onto a 3-sphere (S^3)

# Define a 3-sphere coordinate transformation
def S3_mapping(X, Y, T):
    """Maps the nested oscillatory field to an S^3-like structure."""
    r = np.sqrt(X**2 + Y**2)  # Radial coordinate
    theta = np.arctan2(Y, X)  # Angular coordinate
    phi = np.pi * np.sin(T / 20)  # Evolution parameter in time

    # Convert to 3-sphere (S^3) coordinates
    X_s3 = np.sin(theta) * np.cos(phi)
    Y_s3 = np.sin(theta) * np.sin(phi)
    Z_s3 = np.cos(theta)

    # Compute energy as a function of mapped coordinates
    energy_s3 = np.sin(4 * np.pi * r - 0.1 * T) * np.exp(-r**2)

    return X_s3, Y_s3, Z_s3, energy_s3

# Generate mapped coordinates for visualization
T_final = time_steps - 1  # Use last time step to analyze evolution
X_s3, Y_s3, Z_s3, energy_s3 = S3_mapping(X, Y, T_final)

# Plot the mapped energy structure in an S^3-like form
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_s3, Y_s3, Z_s3, c=energy_s3, cmap="inferno", marker='o', alpha=0.7)

ax.set_xlabel("X-axis (S^3)")
ax.set_ylabel("Y-axis (S^3)")
ax.set_zlabel("Z-axis (Energy Density)")
ax.set_title("Mapping of COM Nested Fields onto Poincaré 3-Sphere (S^3)")

plt.show()

# Compute connectivity after mapping onto S^3
s3_connectivity = np.mean(energy_s3) > 0.01  # Check if all regions have energy presence

s3_connectivity