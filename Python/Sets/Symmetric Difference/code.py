# Enter your code here. Read input from STDIN. Print output to STDOUT# Read the inputs
M = int(input())
set_M = set(map(int, input().split()))
N = int(input())
set_N = set(map(int, input().split()))

# Compute the symmetric difference
symmetric_diff = set_M.symmetric_difference(set_N)

# Sort the symmetric difference in ascending order
sorted_diff = sorted(symmetric_diff)

# Print the symmetric difference integers, one per line
for num in sorted_diff:
    print(num)
