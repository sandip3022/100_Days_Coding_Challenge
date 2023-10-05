"""
Day 9: Write a program to count number of digit.

test Case
Input: 7853
Output: 4

Intput : 435
Output: 3
"""
def NoOfDigit(N):
    digit = 0
    while (N):
        digit= digit + 1
        N= N//10
    return digit
N = int(input("Enter any intger-:"))
print("Number of digits in the given number :", NoOfDigit(N))