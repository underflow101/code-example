# findParts_set.py
# book p.197

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in arr:
        print('yes', end=' ')
    else:
        print('no', end=' ')