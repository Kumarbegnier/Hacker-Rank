Polar coordinates are an alternative way of representing Cartesian coordinates or Complex Numbers.
A complex number z
Capture.PNG
z = x + yj
is completely determined by its real part and imaginary party. Here, j is the imaginary unit.
![image](https://github.com/Kumarbegnier/Hacker-Rank/assets/49531334/8e578b81-2a35-4185-bba4-c06275d1a6d8)
→ Polar Axis
A polar coordinate (r, c)
is completely determined by modulus and phase angle .
If we convert complex number z to its polar coordinate, we find:
r: Distance from z to origin, i.e., √x2 + y2
y: Counter clockwise angle measured from the positive x-axis to the line segment that joins z to the origin.
Python's cmath module provides access to the mathematical functions for complex numbers.
cmath.phase
This tool returns the phase of complex number z (also known as the argument of z).                                                       >>> phase (complex (-1.0, 0.0))
3.1415926535897931
abs
This tool returns the modulus (absolute value) of complex number z.
>>> abs (complex (-1.0, 0.0))
1.0
Task
You are given a complex z. Your task is to convert it to polar coordinates.
Input Format
A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a
complex number.
Constraints
Given number is a valid complex number
Output Format
Output two lines:
The first line should contain the value of *.
The second line should contain the value of p.
Sample Input
1+2j
Sample Output
2.23606797749979
1.1071487177940904
Note: The output should be correct up to 3 decimal places.
