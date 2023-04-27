There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist. Example
a = [2,6]
b = [24,36]
There are two numbers between the arrays: 6 and 12.
6%20,6%60,24%60 and 36%6 = 0 for the first value.
12%20,12%60 and 24%12 = 0,36%12 = 0 for the second value. Return 2.
Function Description
Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
getTotalX has the following parameter(s):
⚫int a[n]: an array of integers
⚫ int b[m]: an array of integers
Returns
⚫int: the number of integers that are between the sets
Input Format
The first line contains two space-separated integers, and m, the number of elements in arrays & and b.
The second line contains distinct space-separated integers a[] where 0 ≤ i<n.
The third line containsm distinct space-separated integers b[j] where 0 ≤ j <m..
Constraints
• 1 ≤ n,m ≤ 10 • 1 ≤ a[i] < 100 • 1<b[j] ≤ 100
Sample Input
23
24
16 32 96                                                                                                                                                                                                                             Sample Output
3
Explanation
2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.
4, 8
a
n
d
1
6
a
r
e
t
h
e
o
nly
t
h
r
e
e
n
u
m
b
e
r
s
f
o
r
w
hic
h
e
a
c
h
ele
m
e
n
t
o
f
a is
a
f
a
c
t
o
r
a
n
d
e
a
c
h is
a
f
a
c
t
o
r
o
f
all elements of b.
