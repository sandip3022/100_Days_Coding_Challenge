'''Day 10 coding Statement:  Write a program to find Factorial of a number
Description
Get a number from user for which you need to fin the factorial, then calculate the factorial and give it as the output.
Input

4
Output
24'''

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input())
print(fact(n))