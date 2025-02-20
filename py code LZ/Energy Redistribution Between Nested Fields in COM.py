# Simulating Energy Redistribution Between Nested Fields

# Define an updated function for local field interactions
def energy_exchange(X, Y, t):
    """Models how energy flows between nested oscillatory pockets."""
    r = np.sqrt(X**2 + Y**2)  # Radial distance
    wave1 = np.sin(4 * np.pi * r - 0.1 * t) * np.exp(-r**2)  # First field wave
    wave2 = np.cos(6 * np.pi * r - 0.15 * t) * np.exp(-r**2 / 2)  # Second field wave
    return wave1 + wave2  # Superposition of multiple energy pockets

# Initialize the simulation for energy exchange
energy_flow_evolution = np.zeros((grid_size, grid_size, time_steps))

# Simulate time evolution for energy transfer
for t in range(time_steps):
    energy_flow_evolution[:, :, t] = energy_exchange(X, Y, t)

# Visualize the final time step of energy redistribution
plt.figure(figsize=(6, 6))
plt.imshow(energy_flow_evolution[:, :, -1], cmap="inferno", extent=(-2, 2, -2, 2))
plt.colorbar(label="Energy Flow Density")
plt.title("Energy Redistribution Between Nested Fields in COM")
plt.xlabel("X-Axis (Local Field)")
plt.ylabel("Y-Axis (Nested Energy Pockets)")
plt.show()

# Store the full dataset for further analysis
energy_flow_evolution.shape