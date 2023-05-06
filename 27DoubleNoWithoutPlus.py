'''Day 27 coding Statement : Write a program to find the double of the given number without using arithmetic operator
Description
For the given input number calculate the double of it without using arithmetic operator.

Input
4

Output
8'''

n = int(input())
#print(bin(n))  //4 = 0b100
ans = n<<1 # left shift operator
# print(bin(ans)) // 8 = 0b1000
print(ans)