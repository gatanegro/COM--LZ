# Detect energy pockets by identifying high-density stable regions

# Define a threshold for "high-energy pockets" (peaks in energy density)
energy_threshold = np.percentile(energy_density, 90)  # Top 10% highest energy

# Create a binary mask to identify high-energy pockets
energy_pockets = np.where(energy_density >= energy_threshold, 1, 0)

# Count the number of distinct energy pockets (connected components in high-energy regions)
from scipy.ndimage import label

labeled_pockets, num_pockets = label(energy_pockets)

# Visualize energy pockets in COM
plt.figure(figsize=(6, 6))
plt.imshow(labeled_pockets, cmap="coolwarm", origin="lower")
plt.colorbar(label="Energy Pocket ID")
plt.title(f"Detected Energy Pockets in COM (Total: {num_pockets})")
plt.show()

# Return the number of detected energy pockets
num_pockets