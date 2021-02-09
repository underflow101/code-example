# BOJ 14496
# yaminjeongum

from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
family = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
res = [0 for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    family[i].append(j)
    family[j].append(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        fam = q.popleft()
        for i in family[fam]:
            if not visited[i]:
                visited[i] = True
                res[i] = res[fam] + 1
                q.append(i)

if a == b:
    print(0)
else:
    bfs(a)
    print(res[b] if res[b] != 0 else -1)