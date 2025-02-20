import matplotlib.patches as patches

# Poincaré Disk Representation for Hyperbolic Embedding
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# Draw the unit disk (Poincaré model boundary)
circle = patches.Circle((0, 0), 1, edgecolor="black", facecolor="none", linewidth=2)
ax.add_patch(circle)

# Place Collatz Octave nodes inside hyperbolic space
angles = np.linspace(0, 2 * np.pi, len(nodes), endpoint=False)
positions = {nodes[i]: (np.cos(angles[i]), np.sin(angles[i])) for i in range(len(nodes))}

# Draw connections based on modular equivalences
for (a, b) in edges:
    x_vals = [positions[a][0], positions[b][0]]
    y_vals = [positions[a][1], positions[b][1]]
    ax.plot(x_vals, y_vals, "b", alpha=0.6)

# Draw nodes
for node in nodes:
    ax.plot(*positions[node], "ro", markersize=6)
    ax.text(positions[node][0] * 1.1, positions[node][1] * 1.1, str(node), fontsize=12, ha="center")

ax.set_title("Hyperbolic Embedding of COM in Poincaré Disk")
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.show()