#Program to check entered number is perfect number or not

N = int(input("Enter any number-:"))
sum = 0
for i in range(1,N):
    if(N%i==0):
        sum = sum+i
 
if(N==i):
    print("Enter number is perfect number")
else:
    print("Enter number is not perfect number")