'''Day 45 coding Statement : Write Program to find smallest and largest element in an array

Description

Get an array as input from the user and then find the smallest and largest element in the array.
Input
Enter the size of array :
5
Enter the elements :
10 20 5 40 30

Output
Smallest Number :
5
Largest Number :
40'''

n = int(input("Enter the size of array: "))
arr = list(map(int,input("Enter elements of array:").split(" ")))

mn = min(arr)
mx = max(arr)
print(f"Smallest number:\n{mn}")
print(f"Largest number:\n{mx}")