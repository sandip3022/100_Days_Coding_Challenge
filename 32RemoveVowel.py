'''Day 32 coding Statement : Write a Program to Remove vowels from a string

Description
Get a string as the input from the user and then remove all the vowel letters from the string and give the output.

Input
remove

Output
rmv'''

s = input()
a = ""
vowel = "AEIOUaeiou"
for i in s:
    if i not in vowel:
        a+=i
print(a)