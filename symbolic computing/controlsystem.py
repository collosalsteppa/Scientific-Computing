import sympy as sp

# Define the variable
s = sp.symbols('s')

# Define the transfer function H(s)
H = 1 / (s**2 + 3*s + 2)

# Step 1: Factor the denominator
denominator = s**2 + 3*s + 2
factored_denominator = sp.factor(denominator)
print(f"Factored Denominator: {factored_denominator}")

# Step 2: Compute the inverse Laplace Transform to find h(t)
h_t = sp.inverse_laplace_transform(H, s, sp.symbols('t'))
print(f"Inverse Laplace Transform h(t): {h_t}")

# Step 3: Find the poles of the system
poles = sp.solve(denominator, s)
print(f"Poles of the system: {poles}")