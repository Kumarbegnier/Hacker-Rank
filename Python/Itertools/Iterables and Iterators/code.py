from itertools import combinations

# Read input
N = int(input())
letters = input().strip()
K = int(input())

# Calculate the total number of combinations
total_combinations = len(list(combinations(range(1, N+1), K)))

# Calculate the number of combinations with 'a'
combinations_with_a = 0
for comb in combinations(range(1, N+1), K):
    if any(letters[i-1] == 'a' for i in comb):
        combinations_with_a += 1

# Calculate the probability
probability = combinations_with_a / total_combinations

# Print the result with 3 decimal places
print("{:.4f}".format(probability))
