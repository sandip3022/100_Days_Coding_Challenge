'''Day 34 coding Statement : Write a Program to Remove brackets from an algebraic expression
Description
Get an algebraic expression as input from the user and then remove all the brackets in that.

Input
7x+(2*y)

Output
7x+2*y'''

s = input()
a = ""
for i in s:
    if i == "(" or i == ")":
        a+=""
    else:
        a+=i
print(a)
