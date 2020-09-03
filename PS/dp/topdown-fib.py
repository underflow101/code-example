# topdown-fib.py
# book p.212

import sys
from collections import deque
input = sys.stdin.readline

d = [0] * 100

def fib(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

print(fib(99))