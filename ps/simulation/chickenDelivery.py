# chickenDelivery.py
# book p.332

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    res = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in candidate:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        res += tmp
    return res

res = 1e9
for candidate in candidates:
    res = min(res, get_sum(candidate))
    
print(res)