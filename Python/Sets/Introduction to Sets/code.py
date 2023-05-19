def average(arr):
    distinct_heights = set(arr)  # Create a set of distinct heights
    total_heights = sum(distinct_heights)  # Compute the sum of distinct heights
    num_heights = len(distinct_heights)  # Compute the total number of distinct heights
    avg = total_heights / num_heights  # Compute the average
    return round(avg, 3)  # Return the average rounded to 3 decimal places


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
