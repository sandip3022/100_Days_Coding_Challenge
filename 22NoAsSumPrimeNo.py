'''Day 22 coding Statement : Write a program to express a number as a sum of two prime numbers

Description
Get a number as input from the user and express that number as sum of two prime numbers.

Input
4

Output
4 can be expressed as sum of 2 and 2'''

num = int(input())
prime = []
for i in range(2,num):
    flag = False
    for j in range(2,i):
        if i%j==0:
            flag = True
            break
    if not flag:
        prime.append(i)

ans = []
for i in prime:
    for j in prime:
        if i+j== num:
            ans=[i,j]
            break
if ans:
    print( num,"can be expressed as sum of {} and {}".format(ans[0],ans[1]))
else:
    print(f"{num} can not express as num of two prime number")
    


