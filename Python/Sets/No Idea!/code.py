# Enter your code here. Read input from STDIN. Print output to STDOUT# Read the inputs
n, m = map(int, input().split())
array = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

# Calculate the happiness score
happiness = 0
for num in array:
    if num in set_A:
        happiness += 1
    elif num in set_B:
        happiness -= 1

# Print the final happiness score
print(happiness)
