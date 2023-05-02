'''Day 6 coding Statement:  Write a program to find the Quadrants in which coordinates lie

Get the value of x and y coordinates as input from the user and check in which quadrant the point lies and print it.

Input
10 20
Output
This point lies in first quadrant.

Input
-10 20
Output
This point lies in second quadrant. '''

x,y = list(map(int,input().split(" ")))

if x >0:
    if y > 0:
        print("This point lies in first quadrant.")
    else:
        print("This point lies in second quadrant.")
else:
    if y > 0:
        print("This point lies in third quadrant.")
    else:
        print("This point lies in fourth quadrant.")
    
        