'''Day 48 coding Statement : Write Program to remove duplicate elements in an array

Description
Get an array as input from the user and then remove all the duplicate elements in that array.

Input
Enter the size of array
5

Enter the elements of array
35 35 45 60 60

Output
35 45 60
'''

n = int(input("Enter the size of array: "))
arr = list(map(int,input("Enter elements of array:").split(" ")))

s = set(arr)
for i in list(s):
    print(i,end=" ")
    