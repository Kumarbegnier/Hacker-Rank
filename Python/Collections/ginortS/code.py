s = input()

# define the sorting key function
def custom_sort_key(c):
    if c.islower():
        return ord(c)
    elif c.isupper():
        return ord(c) + 1000
    elif c.isdigit():
        if int(c) % 2 == 1:
            return ord(c) + 2000
        else:
            return ord(c) + 3000

# sort the string using the custom key function
sorted_s = sorted(s, key=custom_sort_key)

# convert the sorted list back to a string and print it
print(''.join(sorted_s))
