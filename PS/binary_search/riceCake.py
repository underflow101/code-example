# riceCake.py
# book p.201

import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

start = 0
end = max(arr)
res = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)