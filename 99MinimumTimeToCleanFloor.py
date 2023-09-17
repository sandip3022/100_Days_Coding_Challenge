"""
Day 99 coding Statement :
There is a hallway of length N−1 and you have M workers to clean the floor. Each worker is responsible for segment [Li?,Ri?], i.e., the segment starting at Li? and ending at Ri?. The segments might overlap.
Every unit of length of the floor should be cleaned by at least one worker. A worker can clean 1 unit of length of the floor in 1 unit of time and can start from any position within their segment. 
A worker can also choose to move in any direction. However, the flow of each worker should be continuous, i.e, they can’t skip any portion and jump to the next one, though they can change their direction. 
What’s the minimum amount of time required to clean the floor, if the workers work simultaneously?

Input:
First line will contain T, number of testcases. Then the testcases follow. Each testcase contains of M+1 lines of input. First line contains 22 space separated integers N, M, length of the hallway and number of workers. 
Each of the next M lines contain 2 space separated integers Li?, Ri?, endpoints of the segment under ith worker. 

Output: For each testcase, output in a single line minimum time required to clean the hallway or −1 if it's not possible to clean the entire floor.
Sample Input

3
10 3
1 10
1 5
6 10
10 1
2 10
10 2
5 10
1 5

Sample Output

3
-1
5
"""

for _ in range(int(input())):
    n, m = map(int, input().split())
    segments = []
    
    for _ in range(m):
        li, ri = map(int, input().split())
        segments.append((li, ri))
    
    segments.sort()
    rightmost = -1
    time = 0
    
    for li, ri in segments:
        if li > rightmost:
            time += li - rightmost - 1
            rightmost = ri
        elif ri > rightmost:
            rightmost = ri
    
    if rightmost < n:
        time += n - rightmost
    
    print(time)
