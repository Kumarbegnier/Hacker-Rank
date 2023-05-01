def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        t = string[i:i+k]
        u = []
        for c in t:
            if c not in u:
                u.append(c)
        print(''.join(u))


if __name__ == '__main__':
