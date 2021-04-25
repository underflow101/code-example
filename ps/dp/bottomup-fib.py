# bottomup-fib.py
# book p.215

import sys
from collections import deque
input = sys.stdin.readline

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])