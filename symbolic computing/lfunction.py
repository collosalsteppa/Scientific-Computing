import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the loss function
L = 3*x**2 + 2*x - 5

# Compute the first derivative (gradient)
L_prime = sp.diff(L, x)
print(f"First derivative (gradient): L'(x) = {L_prime}")

# Solve for x when the gradient is zero
critical_points = sp.solve(L_prime, x)
print(f"Critical points (where gradient is zero): {critical_points}")

# Compute the second derivative
L_double_prime = sp.diff(L_prime, x)
print(f"Second derivative: L''(x) = {L_double_prime}")

# Check if the critical points are minima or maxima
for point in critical_points:
    concavity = L_double_prime.subs(x, point)
    if concavity > 0:
        print(f"x = {point} is a minimum.")
    elif concavity < 0:
        print(f"x = {point} is a maximum.")
    else:
        print(f"x = {point} is an inflection point.")
