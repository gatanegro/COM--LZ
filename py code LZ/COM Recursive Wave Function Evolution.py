# Simulating COM's Recursive Evolution Over Multiple Loops

# Define the number of iterations (nested loops) to compute
num_iterations = 100

# Initialize the wave function values
psi_values = np.zeros(num_iterations)
psi_values[0] = 1  # Initial condition

# Compute the evolution of the recursive wave equation
for i in range(1, num_iterations):
    psi_values[i] = np.sin(psi_values[i-1]) + np.exp(-psi_values[i-1])

# Plot the evolution of the recursive COM function
plt.figure(figsize=(8, 4))
plt.plot(range(num_iterations), psi_values, marker="o", linestyle="-", color="blue", label="Ψ(n) Evolution")
plt.xlabel("Recursion Level (n)")
plt.ylabel("Wave Function Ψ(n)")
plt.title("COM Recursive Wave Function Evolution")
plt.legend()
plt.grid(True)
plt.show()

# Display the computed recursive values
psi_values

Result
array([1.        , 1.20935043, 1.23377754, 1.23493518, 1.23498046,
       1.23498221, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228,
       1.23498228, 1.23498228, 1.23498228, 1.23498228, 1.23498228])
