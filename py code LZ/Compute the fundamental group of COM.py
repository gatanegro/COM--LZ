# Compute the fundamental group of COM

from sympy import symbols, Matrix

# Define symbolic variables for path loops
x, y, z = symbols('x y z')

# Define fundamental group generators (approximating a 3-manifold structure)
# A simple representation of loops around COM
loop_1 = Matrix([sin(x), cos(y), sin(z)])  # Small loop around a node
loop_2 = Matrix([cos(x), sin(y), cos(z)])  # Another loop

# Compute the commutator of these loops to check for non-triviality
commutator = loop_1.cross(loop_2)  # Cross product simulates group multiplication

# Check if the commutator simplifies to zero (trivial fundamental group)
trivial_fundamental_group = all(sp.simplify(val) == 0 for val in commutator)
trivial_fundamental_group