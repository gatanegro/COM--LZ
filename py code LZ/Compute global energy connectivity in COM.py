# Compute global energy connectivity in COM

# Define a connectivity matrix for energy transitions
connectivity_matrix = np.zeros((len(nodes), len(nodes)))

# Fill the matrix based on energy flow transitions (modular arithmetic structure)
for (a, b) in edges:
    connectivity_matrix[a - 1, b - 1] = 1  # Mark connection (1-based index adjustment)
    connectivity_matrix[b - 1, a - 1] = 1  # Ensure symmetry

# Compute the eigenvalues of the connectivity matrix
eigenvalues = np.linalg.eigvals(connectivity_matrix)

# Check if the smallest eigenvalue is zero (indicating a fully connected structure)
is_fully_connected = min(eigenvalues) == 0

is_fully_connected