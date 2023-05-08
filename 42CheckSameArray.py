'''Day 42 coding Statement : Write Program to check if two arrays are the same or not

Description

Get two arrays as the input from the user and check whether it is the same or not.

Input
Enter the size of first array :
3

Enter the size of second array :
3

Enter elements of first array :
1 2 3

Enter elements of second array :
1 2 3

Output
Same'''

l1 = int(input("Enter length of first array: "))
l2 = int(input("Enter length of second array:"))

arr1 = list(map(int,input().split(" ")))
arr2 = list(map(int,input().split(" ")))
flag = True
for i in range(l1):
    if arr1[i] != arr2[i]:
        flag = False
if flag:
    print("Same")
else:
    print("Not Same")