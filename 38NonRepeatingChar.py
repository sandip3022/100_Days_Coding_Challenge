'''Day 38 coding Statement : Write a Program to print Non-repeating characters in a string
Description
Get a string as the input from the user and print the non-repeating characters in a string.

Input
Hello

Output
H e o'''

s = input()
for i in s:
    if s.count(i) == 1:
        print(i,end=" ")