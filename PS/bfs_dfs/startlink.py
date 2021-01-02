# BOJ 5014
# startlink

from collections import deque

f, s, g, u, d = map(int, input().split())
d = -d
aim = s - g
visited = [False for _ in range(f+1)]
visited[s] = True

def bfs(now):
    global u, d, f, g
    
    if now == g:
        return 0
    
    q = deque()
    q.append((now, 0))
    
    while q:
        x, cnt = q.popleft()
        for nx in (x + u, x + d):
            if nx < 1 or nx > f:
                continue
            if nx == g:
                return cnt + 1
            if not visited[nx]:
                visited[nx] = True
                q.append((nx, cnt+1))
    return -1

res = bfs(s)
if res == -1:
    print("use the stairs")
else:
    print(res)