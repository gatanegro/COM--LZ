# Navier-Stokes Simulation for Energy Flow in the Collatz Octave Model

# Define parameters for fluid simulation
grid_size = 50  # 50x50 grid for fluid dynamics
viscosity = 0.1  # Viscosity of the field (affects flow stability)
dt = 0.01  # Time step

# Initialize velocity and energy density fields
velocity_x = np.zeros((grid_size, grid_size))
velocity_y = np.zeros((grid_size, grid_size))
energy_density = np.zeros((grid_size, grid_size))

# Place initial energy values in a circular pattern
center = grid_size // 2
radius = grid_size // 4

for i in range(grid_size):
    for j in range(grid_size):
        # Compute distance from center
        dist = np.sqrt((i - center) ** 2 + (j - center) ** 2)
        if radius - 2 < dist < radius + 2:  # Circular energy node placement
            angle = np.arctan2(j - center, i - center)
            energy_density[i, j] = np.sin(8 * angle)  # Oscillatory field energy
            velocity_x[i, j] = np.cos(angle) * 0.1  # Initial circular velocity
            velocity_y[i, j] = np.sin(angle) * 0.1

# Function to simulate energy transport (simplified Navier-Stokes update)
def update_fluid(energy, vel_x, vel_y, dt, viscosity):
    # Compute Laplacian for diffusion
    laplacian = (
        np.roll(energy, 1, axis=0) + np.roll(energy, -1, axis=0) +
        np.roll(energy, 1, axis=1) + np.roll(energy, -1, axis=1) - 4 * energy
    )

    # Apply viscosity and diffusion step
    energy += viscosity * laplacian * dt

    # Advection step (move energy with velocity field)
    energy = np.roll(energy, shift=int(np.mean(vel_x)), axis=0)
    energy = np.roll(energy, shift=int(np.mean(vel_y)), axis=1)

    return energy

# Run simulation for multiple time steps
time_steps = 100
for _ in range(time_steps):
    energy_density = update_fluid(energy_density, velocity_x, velocity_y, dt, viscosity)

# Plot final energy density distribution
plt.figure(figsize=(6, 6))
plt.imshow(energy_density, cmap="inferno", origin="lower")
plt.colorbar(label="Energy Density")
plt.title("Navier-Stokes Simulation of Energy Flow in COM")
plt.show()