'''Day 24 coding Statement : Write a program to print Pyramid pattern using stars
Description
Get the number of lines as the input and print stars in that many lines or rows in a pyramid shape.

Input
4

Output
  *
 ***
*****
*******'''
n = int(input())
for i in range(1,n+1):
        for k in range(0,n-i):
            print(" ",end="")
        for l in range(0,2*i-1):
            print("*",end="")
        print("\n")