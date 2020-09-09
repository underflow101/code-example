# stringReassemble.py
# book p.322

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

string = input()
res = []
sum = 0
for i in range(len(string)):
    if string[i].isalpha():
        res.append(string[i])
    else:
        sum += int(string[i])

res.sort()
if sum != 0:
    res = ''.join(res) + str(sum)
    print(res)
else:
    print(''.join(res))