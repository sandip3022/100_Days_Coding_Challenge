'''Day 8 coding Statement:  Write a program to find roots of a quadratic equation

Description

Get the values of a, b and c (coefficients of quadratic equation) as input from the user and calculate the roots and print as the output.

Input
Enter the value of a, b and c : 1 -6 9

Output
Roots are equal
Root 1= root 2 = 3.00
'''

import math
a,b,c = list(map(int,input().split(" ")))

if a == 0:
    print("a cannot be zero")
else:
    d = b**2 - 4 * a * c
    root = math.sqrt(abs(d))
    if d > 0:
        print("Two Real Roots")
        print((-b + root)/(2 * a))
        print((-b -root)/(2 * a))
    elif d == 0:
        print("Roots are equal")
        print(-b / (2*a))
    else:
        print("No Real Root")
        print(- b / (2*a) , " + i", root)
        print(- b / (2*a) , " - i", root)
