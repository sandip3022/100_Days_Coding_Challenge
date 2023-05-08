'''Day 44 coding Statement : Write Program to find number of even and odd elements in an array

Description

Get an array as input from the user and then count the number of even and odd elements present in the array.

Input
Enter size of array

4
Enter the elements :

1 3 4 5
Output

Number of even elements :
1

Number of odd elements :
3
'''

n = int(input("Enter size of array: "))
arr = list(map(int,input().split(" ")))
e = 0
o = 0
for i in arr:
    if i%2 == 0:
        e+=1
    else:
        o+=1
print(f"Number of even elements:\n{e}")
print(f"Number of odd elements:\n{o}")