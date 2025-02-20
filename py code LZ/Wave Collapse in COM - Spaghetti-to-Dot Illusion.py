# Simulating Wave Collapse in COM (Spaghetti-to-Dot Illusion)

# Define wave collapse function based on dynamic energy density redistribution
def wave_collapse(X, Y, t):
    """Simulates how wave structures collapse into localized energy nodes."""
    r = np.sqrt(X**2 + Y**2)  # Radial distance

    # Wave function simulating spaghetti-like elongation
    wave_spaghetti = np.sin(6 * np.pi * r - 0.2 * t) * np.exp(-r**2)

    # Wave collapse into dot-like form (localized energy density node)
    wave_dot = np.exp(-10 * r**2) * np.sin(8 * np.pi * r - 0.3 * t)

    # Superposition of wave elongation (spaghetti) and collapse (dot formation)
    return wave_spaghetti + wave_dot

# Simulate wave collapse evolution over time
wave_collapse_evolution = np.zeros((grid_size, grid_size, time_steps))

for t in range(time_steps):
    wave_collapse_evolution[:, :, t] = wave_collapse(X, Y, t)

# Visualize the final state of wave collapse (dot formation)
plt.figure(figsize=(6, 6))
plt.imshow(wave_collapse_evolution[:, :, -1], cmap="inferno", extent=(-2, 2, -2, 2))
plt.colorbar(label="Collapsed Energy Density")
plt.title("Wave Collapse in COM - Spaghetti-to-Dot Illusion")
plt.xlabel("X-Axis (Field Evolution)")
plt.ylabel("Y-Axis (Localized Mass Illusion)")
plt.show()

# Store data for further time evolution analysis
wave_collapse_evolution.shape