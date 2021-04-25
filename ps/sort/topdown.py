# topdown.py
# book p.178

import sys
from collections import deque
input = sys.stdin.readline

res = list()

n = int(input())
for _ in range(n):
    res.append(int(input()))

res.sort(reverse=True)

for i in res:
    print(i, end=' ')