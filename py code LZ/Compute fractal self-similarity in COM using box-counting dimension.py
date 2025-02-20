# Compute fractal self-similarity in COM using box-counting dimension

import scipy.spatial

# Define a function to compute fractal dimension using the box-counting method
def fractal_dimension(Z, threshold=0.9):
    """Computes the fractal dimension of a 2D energy field using box-counting."""
    def box_count(Z, k):
        """Count the number of non-empty kxk boxes covering the high-energy regions."""
        S = np.add.reduceat(
            np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
            np.arange(0, Z.shape[1], k), axis=1
        )
        return np.count_nonzero(S)

    # Normalize energy density and threshold
    Z = (Z - Z.min()) / (Z.max() - Z.min())  # Normalize values between 0 and 1
    Z = Z > threshold  # Apply threshold to focus on high-energy areas

    sizes = 2**np.arange(1, 6)  # Box sizes (powers of 2)
    counts = np.array([box_count(Z, size) for size in sizes])

    # Fit a line to log-log data to estimate the fractal dimension
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
    return -coeffs[0]  # Fractal dimension is the negative slope

# Compute fractal dimension of COM energy distribution
fractal_dim = fractal_dimension(energy_density)

# Display the result
fractal_dim
