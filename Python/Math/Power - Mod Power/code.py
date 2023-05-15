a = int(input())  # Read the value of a
b = int(input())  # Read the value of b
m = int(input())  # Read the value of m

result1 = pow(a, b)  # Calculate a^b
result2 = pow(a, b, m)  # Calculate (a^b) % m

print(result1)  # Print the result of a^b
print(result2)  # Print the result of (a^b) % m
