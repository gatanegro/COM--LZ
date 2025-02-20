# Compute toroidal mapping for COM (nested standing waves on a torus)

# Define toroidal coordinate transformation
def toroidal_mapping(X, Y, T):
    """Maps the nested oscillatory field onto a toroidal structure."""
    R = 1.5  # Major radius of the torus
    r = 0.5  # Minor radius of the torus

    theta = np.arctan2(Y, X)  # Angle around the central axis
    phi = np.pi * np.sin(T / 20)  # Evolution parameter in time

    # Convert to toroidal coordinates
    X_torus = (R + r * np.cos(phi)) * np.cos(theta)
    Y_torus = (R + r * np.cos(phi)) * np.sin(theta)
    Z_torus = r * np.sin(phi)

    # Compute energy as a function of toroidal coordinates
    energy_torus = np.sin(4 * np.pi * np.sqrt(X**2 + Y**2) - 0.1 * T) * np.exp(-X**2 - Y**2)

    return X_torus, Y_torus, Z_torus, energy_torus

# Generate mapped coordinates for the toroidal model
X_torus, Y_torus, Z_torus, energy_torus = toroidal_mapping(X, Y, T_final)

# Plot the mapped energy structure on a torus
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_torus, Y_torus, Z_torus, c=energy_torus, cmap="inferno", marker='o', alpha=0.7)

ax.set_xlabel("X-axis (Torus)")
ax.set_ylabel("Y-axis (Torus)")
ax.set_zlabel("Z-axis (Energy Density)")
ax.set_title("Mapping of COM Nested Fields onto a Toroidal Manifold")

plt.show()

# Compute connectivity after mapping onto a torus
torus_connectivity = np.mean(energy_torus) > 0.01  # Check if all regions have energy presence

torus_connectivity