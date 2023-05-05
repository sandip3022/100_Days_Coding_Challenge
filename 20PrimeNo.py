'''Day 20 coding Statement : Write a program to identify if the number is Prime number or not

Description
Get a number as input from the user and check whether that number is prime or not.
A prime number is a number with factors as 1 and that number itself.

Input
1

Output
1 is not a prime number

Input
5

Output
5 is a prime number'''

num = int(input())
flag = False
for i in range(2,num):
    if num%i==0:
        flag = True
        break
if flag:
    print(num,"is not prime number")
else:
    print(num,"is prime number")

