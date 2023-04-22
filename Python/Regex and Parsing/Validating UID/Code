import re

def is_valid_uid(uid):
    # Check if UID contains at least 2 uppercase English alphabet characters
    if not re.search(r'[A-Z].*[A-Z]', uid):
        return False

    # Check if UID contains at least 3 digits (0-9)
    if not re.search(r'\d.*\d.*\d', uid):
        return False

    # Check if UID contains only alphanumeric characters and has no repeated characters
    if not re.match(r'^[a-zA-Z0-9]{10}$', uid) or re.search(r'(.).*\1', uid):
        return False

    return True

# Read the number of test cases
t = int(input())

# Process each test case
for i in range(t):
    uid = input().strip()
    if is_valid_uid(uid):
        print('Valid')
    else:
        print('Invalid')
