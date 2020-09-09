# selectBowlingBall.py
# book p.315

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
data = list(map(int, input().split()))

arr = [0] * 11

for x in data:
    arr[x] += 1
    
res = 0
for i in range(1, m+1):
    n -= arr[i]
    res += arr[i]

print(res)