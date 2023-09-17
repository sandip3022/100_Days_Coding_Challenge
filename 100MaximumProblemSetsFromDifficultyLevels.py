"""
Day 100 coding Statement :
You have prepared four problems. The difficulty levels of the problems are A1?,A2?,A3?,A4? respectively. 
A problem set comprises at least two problems and no two problems in a problem set should have the same difficulty level. 
A problem can belong to at most one problem set. Find the maximum number of problem sets you can create using the four problems.

Input Format
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows. 
The first and only line of each test case contains four space-separated integers A1?, A2?, A3?, A4?, denoting the difficulty level of four problems. 
Output Format
For each test case, print a single line containing one integer - the maximum number of problem sets you can create using the four problems.
Sample Input

3
1 4 3 2
4 5 5 5
2 2 2 2
Sample Output

2
1
0
"""
n = int(input())
for i in range(n):
  lis = map(int ,input().split())
  emp = []
  for i in lis:
    if i not in emp:
      emp.append(i)

  l = len(emp)
  if l ==4:
    print("2")
  elif l == 3:
    print("2")
  elif l ==2:
   print("1")
  else:
    print("0")
