"""Day 43 coding Statement : Write Program to find the array type
Description
Get an array as input from the user and check the type of the array, whether it is odd, even or mixed type.

If all the elements of the array are odd, display "Odd".
If all the elements of the array are even, display "Even".
Else, display "Mixed".

Input
Enter size of array :
3

Enter elements 
1 3 5

Output
Odd"""

n = int(input("Enter size of array: "))
arr = list(map(int,input().split(" ")))
e = 0
o = 0
for i in arr:
    if i%2 == 0:
        e+=1
    else:
        o+=1
if e == 0:
    print("Odd")
elif o == 0:
    print("Even")
else:
    print("Mixed")
