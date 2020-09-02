# cardGame.py
# book p.96

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = 0

for i in range(n):
    data = list(map(int, input().split()))
    minval = min(data)
    res = max(res, minval)
print(res)