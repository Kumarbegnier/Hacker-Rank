def swap_case(s):
    new_str = ""
    for char in s:
        if char.isupper():
            new_str += char.lower()
        elif char.islower():
            new_str += char.upper()
        else:
            new_str += char
    return new_str

if __name__ == '__main__':
