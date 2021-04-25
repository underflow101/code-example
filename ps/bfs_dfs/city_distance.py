# city_distance.py
# BOJ 18352
# Book p.339

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n+1)
dist[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if dist[next_node] == -1:
            dist[next_node] = dist[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        check = True
        
if check == False:
    print(-1)