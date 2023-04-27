#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Create a dictionary to count the frequency of each bird type
    freq = {}
    for bird in arr:
        freq[bird] = freq.get(bird, 0) + 1
    
    # Find the bird type with the highest frequency
    max_freq = max(freq.values())
    most_frequent_birds = [bird for bird, count in freq.items() if count == max_freq]
    
    # Return the smallest id of the most frequently sighted birds
    return min(most_frequent_birds)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
