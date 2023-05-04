# write a program to reverse number
# input: 945
# output : 549

N = int(input("Enter any number-:"))
rev= 0
while(N !=0):
 digit = N%10
 rev = rev*10 + digit
 N = N//10 
print(rev)