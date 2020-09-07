# guild.py
# book p.311

import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
data = list(map(int, input().split()))
data.sort()

res = 0
cnt = 0

for i in data:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
print(res)