"""
Alice and Bob went to a pet store. There are N animals in the store where the ith animal is of type Ai?.
Alice decides to buy some of these N animals. Bob decides that he will buy all the animals left in the store after Alice has made the purchase.
Find out whether it is possible that Alice and Bob end up with exactly same multiset of animals.

Input Format:
4
3
4 4 4
4
2 3 3 2
4
1 2 2 3
6
5 5 1 5 1 5
Sample Output

NO
YES
NO
YES
"""

t = int(input())
for i in range(t):
    count = []
    flag = True
    n = int(input())
    lis = list(map(int, input().split(" ")))
    for i in lis:
        c = lis.count(i)
        count.append(c)

    for i in count:
        if i % 2 == 0:
            flag = False

    if flag:
        print("NO")
    else:
        print("YES")
