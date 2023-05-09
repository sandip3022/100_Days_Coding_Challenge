'''
Day 56 coding Statement : Write Program to find whether 
    the numbers of an array be made equal 

Description
Check whether the numbers of array be made equal or not
For eg, for the following input it should print yes because
5023 , 7522 and 150*2 are equal to 300 in all cases. So array numbers can be made equal

Input
3
50 75 150

Output
Yes 
    '''
def checkArr(a,n):
  for i in range(n):
    while (a[i]%2==0):
      a[i] = a[i]/2
    while (a[i]%3==0):
      a[i] = a[i]/3
  for i in range(n):
       if a[i] !=a[0]:
         return False
  return True
    
n=int(input())
arr1 = list(map(int,input().split(" ")))
if checkArr(arr1,n):
  print("Yes")
else:
  print("No")


