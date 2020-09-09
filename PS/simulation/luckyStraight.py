# luckyStraight.py
# book p.321

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

n = list(map(int, input()))
res1 = 0
res2 = 0

if sum(n[:len(n)//2]) == sum(n[len(n)//2:]):
    print("LUCKY")
else:
    print("READY")