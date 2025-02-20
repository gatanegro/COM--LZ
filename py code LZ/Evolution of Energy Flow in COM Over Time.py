# Time-Series Analysis of Energy Flow Stability

# Store energy snapshots over time
energy_snapshots = []

# Run simulation for an extended number of time steps to check stability
extended_time_steps = 200

for _ in range(extended_time_steps):
    energy_density = update_fluid(energy_density, velocity_x, velocity_y, dt, viscosity)
    if _ % 20 == 0:  # Save snapshots every 20 steps
        energy_snapshots.append(energy_density.copy())

# Plot evolution of energy density at different time steps
fig, axes = plt.subplots(1, len(energy_snapshots), figsize=(15, 4))
for i, energy_state in enumerate(energy_snapshots):
    axes[i].imshow(energy_state, cmap="inferno", origin="lower")
    axes[i].set_title(f"Step {i*20}")
    axes[i].axis("off")

plt.suptitle("Evolution of Energy Flow in COM Over Time")
plt.show()