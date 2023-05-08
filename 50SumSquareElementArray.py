'''Day 50 coding Statement : Given an integer array of size N. Write Program to find sum of positive square elements in the array.
Sample input 1 :

4 1 2 3 4
Sample output 1 :
30

Explanation :
(1 + 4 + 9 + 16) = 30

Sample input 2 :
4 -1 -2 -3 -4

Sample output 2 :
30

Explanation :
(1 + 4 + 9 + 16) = 30
'''
arr = list(map(int,input().split(" ")))

s = 0
for i in arr[1:]:
    a = i * i
    s+=a
print(s)