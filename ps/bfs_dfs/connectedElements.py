# BOJ 11724
# connectedElements.py

from collections import deque
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
graph = {}
visited = [False] * 1001
res = 0

for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def bfs(graph, start, visited):
    if visited[start]:
        return False
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()
    
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return True

for i in range(1, n+1):
    if bfs(graph, i, visited):
        res += 1

print(res)