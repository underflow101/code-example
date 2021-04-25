# topology_sort.py
# book p.296
# O (V + E)

import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    res = []
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        res.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in res:
        print(i, end=' ')

topology_sort()