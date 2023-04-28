#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Calculate the total cost of the shared items
    total_cost = sum(bill) - bill[k]
    
    # Calculate the actual amount each person should pay
    actual_share = total_cost // 2
    
    # Check if the calculated amount matches the charged amount
    if b == actual_share:
        print("Bon Appetit")
    else:
        print(b - actual_share)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
