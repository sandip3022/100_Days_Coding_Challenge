'''Day 11 coding Statement:  Write a program to find Fibonacci series up to n
Description
Fibonacci series is a special series where nth term is the sum of previous two terms in the series. The series starts with 0 and 1 as the first and second term of the series respectively.
Here you need to get the value for nth term from user and then print Fibonacci series containing n terms.

Input
5
Output
0,1,1,2,3

Input
8
Output
0,1,1,2,3,5,8,13'''

n = int(input())
a = 0
b = 1
print("0,1",end="")
for i in range(n-2):
    print(",",end="")
    c = a+b
    print(c,end="")
    a = b
    b = c

    