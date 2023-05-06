'''Day 23 coding Statement : Write a program to Replace all 0’s with 1 in a given integer
Description
Get a number as input from the user and find the zeros present in that number.
Then convert the zeros into one and then print it.

Input
310020
Output
311121'''

num = input()
ans=""
for i in num:
    if i == "0":
        ans+="1"
    else:
        ans+=i
print(ans)

