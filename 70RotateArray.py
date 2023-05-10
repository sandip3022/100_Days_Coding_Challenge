'''
Day 70 coding Statement : Given an array, rotate the array by one position in clock-wise direction
Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
Example 2:

Input:
N = 8
A[] = {9, 8, 7, 6, 4, 2, 1, 3}

Output:
3 9 8 7 6 4 2 1

'''

N = int(input())
arr = list(map(int,input().strip().split()))
for i in range(0,1):
  last = arr[len(arr)-1];

for j in range(len(arr)-1,-1,-1):
  arr[j]=arr[j-1]

arr[0]=last;

print( )

for i in range(0,len(arr)):
  print( arr[i] ,end=" ")
