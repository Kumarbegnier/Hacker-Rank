from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    item, price = input().rsplit(' ', 1)
    items[item] = items.get(item, 0) + int(price)

for item, price in items.items():
    print(item, price)
