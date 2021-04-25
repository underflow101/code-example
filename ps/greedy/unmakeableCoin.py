# unmakeableCoin.py
# book p.314

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

n = int(input())
data = list(map(int, input().split()))

data.sort()
target = 1

for x in data:
    if target < x:
        break
    target += x

print(target)