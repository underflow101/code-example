# upsideDownString.py
# book p.313

import sys
from collections import deque, Counter
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

data = input()
cnt0 = 0
cnt1 = 0

if data[0] == '1':
    cnt0 += 1
else:
    cnt1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            cnt0 += 1
        else:
            cnt1 += 1

print(min(cnt0, cnt1))