'''Day 36 coding Statement : Write a Program to Capitalize the first and last letter of each word of a string

Description

Get a string from the user and then change the first and last letter to uppercase.

Input
programming

Output
ProgramminG'''
s = input()
s.capitalize()
ans = s[0].upper()+s[1:-1]+s[-1].upper()
print(ans)
