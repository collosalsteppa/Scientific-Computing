import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the cost function C(x)
C = 5*x**3 - 10*x**2 + 4*x + 3

# Step 1: Find the symbolic derivative of C(x)
C_prime = sp.diff(C, x)
print(f"First derivative (C'(x)): {C_prime}")

# Step 2: Solve for x when the cost is minimized (C'(x) = 0)
critical_points = sp.solve(C_prime, x)
print(f"Critical points (where cost is minimized): {critical_points}")

# Step 3: Compute the second derivative to check if it's a minimum or maximum
C_double_prime = sp.diff(C_prime, x)
print(f"Second derivative (C''(x)): {C_double_prime}")

# Check the concavity at the critical points
for point in critical_points:
    concavity = C_double_prime.subs(x, point)
    if concavity > 0:
        print(f"x = {point} is a minimum.")
    elif concavity < 0:
        print(f"x = {point} is a maximum.")
    else:
        print(f"x = {point} is an inflection point.")