import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Define the Collatz Octave structure
nodes = [1, 2, 3, 4, 5, 6, 7, 8]  # Circular arrangement with 1 in center

# Define energy transitions based on modular arithmetic (mod 3, mod 8)
edges = [
    (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),  # Connections from center
    (2, 4), (3, 6), (4, 8), (5, 2), (6, 5), (7, 3), (8, 7)  # Collatz-style transitions
]

# Create a graph representation
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Assign energy values dynamically based on a wave-like function
energy_values = {n: np.sin(n * np.pi / 4) for n in nodes}

# Draw the network with energy-based coloring
plt.figure(figsize=(6, 6))
pos = {1: (0, 0)}  # Center position for 1
angle_step = 2 * np.pi / 7  # 7 outer nodes in a circular frame

for i, node in enumerate(nodes[1:]):
    pos[node] = (np.cos(i * angle_step), np.sin(i * angle_step))

# Normalize colors for visualization
node_colors = [energy_values[n] for n in nodes]

nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.viridis, node_size=600)
plt.title("Collatz Octave Field Energy Flow (Modular Transitions)")
plt.show()