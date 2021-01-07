# BOJ 1389
# kevin6

from collections import deque

n, m = map(int, input().split())
family = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
res = [0 for _ in range(n+1)]
ans = [0 for _ in range(n+1)]

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

idx = 0
tmp = 1e9
for i in range(1, len(res)):
    bfs(i)
    ans[i] = sum(res)
    visited = [False for _ in range(n+1)]
    res = [0 for _ in range(n+1)]
    if tmp > ans[i]:
        tmp = ans[i]
        idx = i

print(idx)