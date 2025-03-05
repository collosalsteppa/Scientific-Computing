from sympy import symbols, Mod, Eq, solve, mod_inverse

# Define symbols
P, e, N = symbols('P e N')

# Define the encryption function
C = Mod(P**e, N)
print("Symbolic Encryption Function: C =", C)

# Given values
P_val = 7
e_val = 3
N_val = 33

# Compute ciphertext C
C_val = pow(P_val, e_val, N_val)
print(f"Ciphertext (C) for P={P_val}, e={e_val}, N={N_val} is: {C_val}")

# Compute modular inverse of P mod N
try:
    P_inverse = mod_inverse(P_val, N_val)
    print(f"Modular Inverse of P={P_val} mod N={N_val} is: {P_inverse}")
except ValueError:
    print(f"Modular Inverse of P={P_val} mod N={N_val} does not exist.")