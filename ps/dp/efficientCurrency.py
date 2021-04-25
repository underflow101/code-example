# efficientCurrency.py
# book p.226

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list()
for i in range(n):
    arr.append(int(input()))

d = [1001] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)
            
if d[m] == 10001:
    print(-1)
else:
    print(d[m])