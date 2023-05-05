'''Day 19 coding Statement : Write a program to identify if the number is Armstrong number or not
Description
Get an input number from user and check whether the given number is an Armstrong number or not.

E.g. Let the number be 1634,
Here 1^4 + 6^4 + 3 ^4 + 4^4 = 1634
Therefore, this is an Armstrong number

Input
153

Output
Armstrong number

Input
121

Output
Not an Armstrong number  '''

num =  int(input())
pow = len(str(num))
arm = 0
n = num
while n>0:
    digit = n%10
    arm+= digit**pow
    n= n//10
if arm==num:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
