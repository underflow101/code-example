# antWarrior.py
# book p.220

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
d = [0] * 100

# Bottom-up
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arr[i])
    
print(d[n-1])