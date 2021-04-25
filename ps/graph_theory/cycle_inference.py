# cycle_inference.py
# book p.279

import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i
    
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
        
if cycle:
    print("Cycle has happened")
else:
    print("Cycle did not happen")