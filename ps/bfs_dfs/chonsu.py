# BOJ 2644
# chonsu

from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

family = [[] for i in range(n+1)]
visited = [False for i in range(n+1)]
res = [0 for i in range(n+1)]

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

bfs(a)
print(res[b] if res[b] != 0 else -1)