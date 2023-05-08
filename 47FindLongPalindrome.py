'''Day 47 coding Statement : Write Program to find longest palindrome in an array

Description
Get an array as the input from the user and find the longest palindrome in that array.
Input

Enter the size of array
3

Enter the elements of array
121 10456 1000001

Output
1000001'''

n = int(input("Enter the size of array: "))
arr = list(map(int,input("Enter elements of array:").split(" ")))
pali = []
for num  in arr:
    i = str(num)
    rev = i[::-1]
    if rev == i:
        pali.append(num)

print(max(pali))
