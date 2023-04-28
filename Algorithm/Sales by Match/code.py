#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Create an empty dictionary to store the count of each color
    count = {}
    # Initialize the number of pairs to zero
    pairs = 0
    # Loop through the array of colors
    for i in range(n):
        # Get the current color
        color = ar[i]
        # If the color is not in the dictionary, add it with count 1
        if color not in count:
            count[color] = 1
        # If the color is already in the dictionary, increment its count
        else:
            count[color] += 1
            # If the count is even, we have a pair, so increment the pairs count
            if count[color] % 2 == 0:
                pairs += 1
    # Return the number of pairs
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
