from math import comb

def probability_of_a(N, letters, K):
    total_tuples = comb(N, K)
    tuples_without_a = comb(N - letters.count('a'), K)
    tuples_with_a = total_tuples - tuples_without_a
    probability = tuples_with_a / total_tuples
    return round(probability, 4)

# Read input
N = int(input())
letters = input().strip()
K = int(input())

# Calculate probability
probability = probability_of_a(N, letters, K)

# Print the result
print(probability)
