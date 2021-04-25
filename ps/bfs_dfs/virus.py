# BOJ 2606
# virus

from collections import deque

n = int(input())
m = int(input())

network = {}
visited = [False] * (n+1)

for i in range(n):
    network[i+1] = []

for i in range(m):
    _key, _val = map(int, input().split())
    network[_key].append(_val)
    network[_val].append(_key)

def bfs(network, start, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        v = q.popleft()

        for item in network[v]:
            if not visited[item]:
                q.append(item)
                visited[item] = True
        

res = -1
bfs(network, 1, visited)

for i in range(n+1):
    if visited[i]:
        res += 1

print(res)