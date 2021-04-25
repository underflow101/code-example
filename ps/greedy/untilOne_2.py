# untilOne_2.py
# book p.99

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
res = 0

while True:
    target = (n // k) * k
    res += (n - target)
    n = target
    
    if n < k:
        break
    
    res += 1
    n //= k

res += (n - 1)
print(res)