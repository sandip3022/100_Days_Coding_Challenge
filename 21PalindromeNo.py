'''Day 21 coding Statement : Write a program to identify if the number is Palindrome or not
Description
Get a number as input from the user and check whether that number is a Palindrome or not.

Input
121

Output
Palindrome

Input
34

Output
Not a Palindrome'''

num = input()
rev = num[::-1]
if num==rev:
    print("Palindrome")
else:
    print("NOt Palindrome")

