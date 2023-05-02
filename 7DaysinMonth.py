'''Day 7 coding Statement:  Write a program to find Number of days in a given month of a given year
Description
Get the number of month and year as input from the user and check the number of days present in that month.
Input

Enter month : 2
Enter year : 2000

Output
29'''

m = int(input("Enter month :"))
y = int(input("Enter year :"))

if m in (1,3,5,7,8,10,12):
    print("31")
elif m in (4,6,9,11):
    print("30")
else:
    if y%4 == 0:
        print("29")
    else:
        print("28")