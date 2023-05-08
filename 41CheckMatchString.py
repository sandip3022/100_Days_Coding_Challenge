'''Day 41 coding Statement : Check if two strings match where one string contains wildcard characters

Description

Get two strings as input from the user, first with wildcard characters (* and ?) and second without wildcard characters.
Then check whether they match or not.

Input
Ta**nt
Talent

Output
Yes they match'''

def solve(str1,str2):
    a,b = len(str1),len(str2)
    if a==0 and b ==0:
        return True
    if a > 0 and str1[0] == "*" and b == 0:
        return False
    if (a > 1 and str1[0] == "?") or (a!=0 and b!=0 and str1[0]==str2[0]):
        return solve(str1[1:],str2[1:])
    if a !=0 and str1[0] == "*":
        return solve(str1[1:],str2) or solve(str1,str2[1:])
    return False

s1 = input("Enter string with wild characters: ")
s2 = input("Enter string without wild characters: ")

ans = solve(s1,s2)
if ans:
    print("Yes it matches")
else:
    print("No it is not matching")
    
