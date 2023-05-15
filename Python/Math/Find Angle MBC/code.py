import math

AB = int(input())  # Length of side AB
BC = int(input())  # Length of side BC

MBC = round(math.degrees(math.atan(AB / BC)))  # Calculate the arctan of AB/BC in radians and convert it to degrees

print(str(MBC) + "\u00b0")  # Print the rounded value of MBC with the degree symbol
