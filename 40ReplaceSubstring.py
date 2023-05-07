'''Day 40 coding Statement : Write a Program to Replace substring in a string

Description

Get a string as input from the user and then get another string which has to be removed from the string.

Get the third input, the new substring which is placed in that substring position.

Finally print the output by replacing the substring with new string.

Input
Enter a string
talentbattle

Enter the substring to be removed :
talent

Enter the new substring :

student
Output
The new string :
studentbattle'''

s1 = input("Enter a string: ")
s2 = input("Enter string to be removed: ")
s3 = input("Enter new substring: ")
s = s1.replace(s2,s3)
print(s)
