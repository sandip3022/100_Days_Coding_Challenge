#write program to find sum of digit in numbers
# input: 234
# output: 9

N =int(input("Enter a number: "))
Sum=0
while N!=0:
    Sum=Sum+N%10
    N=N//10
print(Sum)