# curriculum.py
# book p.303

import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

v = int(input())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
    
def topology_sort():
    res = list(time)
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            res[i] = max(res[i], res[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, v+1):
        print(res[i])

topology_sort()