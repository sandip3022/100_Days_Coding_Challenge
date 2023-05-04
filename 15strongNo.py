#This is program to find given number is strong no or not
N =int(input("Enter any Number-:"))
temp = N
i = 0
fact = 1
sum=0
while(N !=0):
    rem = N %10
    while(i <=rem):
        fact=fact*i
        i = i+1
    sum = sum + fact
    N = N//10
if(temp==sum):
    print("The entered number is strong number" )
else:
    print("The entered number is not strong number" )
