import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"
    time_1 = datetime.datetime.strptime(t1, format_str)
    time_2 = datetime.datetime.strptime(t2, format_str)
    delta = abs((time_1 - time_2).total_seconds())
    return str(int(delta))

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
