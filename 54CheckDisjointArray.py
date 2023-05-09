'''Day 54 coding Statement : Given an integer array of size N. 
Write Program to find whether Arrays are disjoint or not. 
Two arrays are said to be disjoint if they have no elements in common.
Sample input 1:
4
2 -4 -1 -3
3
1 3 5
Sample output 1:
Disjoint

Sample input 2:
5
1 5 -7 6 3
4
2 4 6 8
Not Disjoint
'''
n1 = int(input())
arr1 = list(map(int,input().split(" ")))
n2 = int(input())
arr2 = list(map(int,input().split(" ")))

disjoint = True
for i in arr1:
    if i in arr2:
        disjoint = False
        break

if disjoint:
    print("Disjoint")
else:
    print("Not Disjoint")