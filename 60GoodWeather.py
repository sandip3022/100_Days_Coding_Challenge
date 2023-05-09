'''
Day 60 coding Statement : Good Weather

The weather report of Magicland is Good if the number of sunny days in a week is strictly greater than the number of rainy days.

Given 7 integers A1,A2,A3,A4,A5,A6,A7 where Ai=1 denotes that the ith day of week in Magicland is a sunny day, Ai=0 denotes that the ith day in Magicland is a rainy day. Determine if the weather report of Magicland is Good or not.

Input Format

First line will contain T, number of testcases. Then the testcases follow.

Each testcase contains of a single line of input, 7 space separated integers A1,A2,A3,A4,A5,A6,A7.

Output Format

For each testcase, print "YES" if the weather report of Magicland is Good, otherwise print "NO". Print the output without quotes.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

Sample Input 1

4
1 0 1 0 1 1 1
0 1 0 0 0 0 1
1 1 1 1 1 1 1
0 0 0 1 0 0 0

Sample Output 1
YES
NO
YES
NO

'''
n = int(input())
weather = []
for i in range(n):
  A = list(map(int,input().split()))
  sum =sum(A)
  if sum >=4:
    status = "yes"
    weather.append(status)
  else:
    status = "no"
    weather.append(status) 
for i in weather:
  print(i)
