"""
Day 72 coding Statement : In this problem you will have to implement a simple editor. 
The editor maintains the content of a string S and have two following functions:

"+ i x": insert a string x into the current string S after the i'th character of the S (we use 1-indexing in this problem). When i equals to 0 it mean we add x at the beginning of S.
"? i len": Print the sub-string of length len starting at position i'th of S. At the beginning, the editor holds an empty string. There will be Q queries of the two types described above.

Input
The first line contains the integer Q. Each line in the next Q lines contains one query.
Output

For each query of the second type, print out the answer sub-string in one line.
Sample Input

5
0 ab
1 c
? 1 3
2 dd
? 1 5

Sample Output
acb
acddb
"""

def insert(string_s,insert_i,pos_i=0):
  return string_s[:pos_i]+insert_i+string_s[pos_i:]

n = int(input())
s = ""
for i in range(n):
  o, ind, st = map(str,input().split())
  index = int(ind)
  if o=="+":
    if o ==0:
      s = s+st
    else:
      s =insert(s,st,index)
  else:
    index1 = int(st)
    print(s[index-1:index+index1-1])