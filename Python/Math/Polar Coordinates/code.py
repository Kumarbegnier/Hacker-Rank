import cmath

z = complex(input())  # Read the complex number

r = abs(z)  # Calculate the modulus (absolute value)
phi = cmath.phase(z)  # Calculate the phase angle

print(round(r, 3))  # Print the modulus rounded to 3 decimal places
print(round(phi, 3))  # Print the phase angle rounded to 3 decimal places
