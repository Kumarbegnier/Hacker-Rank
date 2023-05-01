from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    counter = Counter(s)
    for char, count in sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, count)
