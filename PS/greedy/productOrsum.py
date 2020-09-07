# productOrsum.py
# book p.312

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

data = input()
res = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num < 2 or res < 2:
        res += num
    else:
        res *= num

print(res)