'''Day 25 coding Statement : Write a program to find Area of a circle
Description
Get the value for radius from the user and calculate the area of the circle for the given radius.
Area of circle = 3.14*radius*radius

Input
3

Output
28.27'''

import math
r = int(input())
area  =(math.pi*r*r)
a = round(area,2)
print(a) 