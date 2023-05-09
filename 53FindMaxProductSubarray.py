'''Day 53 coding Statement : Given an integer array of size N.
    Write Program to find maximum product subarray in a given array.
    
Sample input 1:
4
2 -4 -1 -3
Sample output 1:
8 = {2, -4, -1}

Sample input 2:
5
1 5 -7 5 3
Sample output 2:
15 = {5, 3}
    '''

n = int(input())
arr = list(map(int,input().split(" ")))

result = arr[0]
for i in range(n):
    mul = arr[i]
    for j in range(i+1,n):
        result = max(result,mul)
        mul *=arr[j]
    result = max(result,mul)
print(result)