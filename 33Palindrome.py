'''Day 33 coding Statement : Write a Program to check if String is a palindrome or not
Description
Get an input string from the user and then check whether it is a palindrome string or not.

Input
noon

Output
Palindrome

Input
Talent

Output
Not a Palindrome'''

s = input().lower()
rev = s[::-1]
if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")