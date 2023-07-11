# Read the input expression as a string
expression = input()

# Evaluate the expression using eval() and store the result
result = eval(expression)

# Check if the result is None (due to the print statement) and modify it accordingly
if result is None:
    result = ''

# Print the result
print(result)
