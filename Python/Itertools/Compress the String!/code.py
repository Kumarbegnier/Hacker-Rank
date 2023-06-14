from itertools import groupby

def compress_string(s):
    compressed_string = ""
    for key, group in groupby(s):
        count = len(list(group))
        compressed_string += f"({count}, {key}) "
    return compressed_string.rstrip()

# Read input string
s = input()

# Compress the string
compressed = compress_string(s)

# Print the compressed string
print(compressed)
