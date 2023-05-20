from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
total_marks = sum([int(Student._make(input().split()).MARKS) for _ in range(n)])
average = total_marks / n
print(f'{average:.2f}')
