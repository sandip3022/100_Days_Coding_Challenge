"""Day 46 coding Statement : Write Program to find sum of elements in an array
Description
Get an array as the input from the user and find the sum of the elements.

Input

Enter the size of array
3

Enter the elements of array
5 10 15

Output
30"""

n = int(input("Enter the size of array: "))
arr = list(map(int,input("Enter elements of array:").split(" ")))

s = sum(arr)
print(s)