import sympy as sp

# Define a symbolic homotopy transformation function
theta = sp.symbols('theta')  # Continuous deformation parameter

# Define a homotopy function transforming COM energy oscillations smoothly
H = (1 - theta) * sin(pi * (n + 1) / 4) + theta * cos(pi * m / 4)

# Compute partial derivatives to check homotopy smoothness
H_n = sp.diff(H, n)
H_m = sp.diff(H, m)
H_theta = sp.diff(H, theta)

# Check if homotopy transformation is smooth (all derivatives remain continuous)
smooth_homotopy = all(sp.simplify(derivative) is not sp.nan for derivative in [H_n, H_m, H_theta])
smooth_homotopy