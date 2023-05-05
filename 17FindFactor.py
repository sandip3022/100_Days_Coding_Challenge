'''Day 17 coding Statement : Write a program to find the Factors of a number
Description
Get an input from the user and find the factors of the number.

Input
4
Output
1,2,4'''

n = int(input())

for i in range(1,n+1):
    if n%i==0:
        print(i,end=",")