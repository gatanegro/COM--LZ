# Modify the energy field equation to include a tension component

# Define a new energy function incorporating tension forces
tension_coefficient = 0.1  # Scaling factor for tension influence

# Adjust energy equation by adding a tension correction term
E_tension_corrected = E_solution + tension_coefficient * np.mean(tension_field)

# Recompute connectivity with tensions added
connectivity_matrix_corrected = np.copy(connectivity_matrix)

# Introduce tension-based connectivity corrections
for i in range(len(nodes)):
    for j in range(len(nodes)):
        if i != j:
            # If tension is high, add a weak connection to simulate restructuring
            if tension_field.mean() > 0.2:  
                connectivity_matrix_corrected[i, j] = 1  

# Compute eigenvalues of new connectivity matrix
eigenvalues_corrected = np.linalg.eigvals(connectivity_matrix_corrected)

# Check if global connectivity is restored
is_fully_connected_with_tension = min(eigenvalues_corrected) == 0

is_fully_connected_with_tension