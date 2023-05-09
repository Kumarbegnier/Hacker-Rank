# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input()) # number of shoes in the shop
shoe_sizes = Counter(map(int, input().split())) # sizes of shoes in the shop
n = int(input()) # number of customers
total_money_earned = 0

for i in range(n):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        total_money_earned += price
        shoe_sizes[size] -= 1

print(total_money_earned)
