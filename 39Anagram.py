'''Day 39 coding Statement : Write a Program to check if two strings are Anagram or not

Description
Get two strings as input from the user and check whether it is Anagram or not.

Input
sunlight thgiluns

Output
Anagram
'''
lis = list(input().split(" "))
flag = True
for i in lis[0]:
    if i not in lis[1]:
       flag = False
       break
if flag:
    print("Anagram")
else:
    print("Not Anagram")

