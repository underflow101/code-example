# BOJ 1697
# teleport.py

from collections import deque

LIMIT = 100001
n, k = map(int, input().split())
dist = [0] * LIMIT

def bfs(dist, start, end):
    q = deque([start])
    
    if start == end:
        return 0
    
    while q:
        v = q.popleft()
        
        for i in (v-1, v+1, v*2):
            if 0 <= i < LIMIT:
                if dist[i] == 0:
                    dist[i] = dist[v] + 1
                    q.append(i)
                if i == end:
                    return dist[i]
                
print(bfs(dist, n, k))