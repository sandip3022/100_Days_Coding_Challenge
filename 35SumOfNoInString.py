'''Day 35 coding Statement : Write a Program to Count the sum of numbers in a string
Description
Get a string from the user and find the sum of numbers in the string.

Input
Hello56

Output
11'''

s = input()
sum = 0
for i in s:
    if i.isdigit():
        sum +=int(i)
print(sum)