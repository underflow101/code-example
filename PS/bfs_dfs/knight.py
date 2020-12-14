# BOJ 7562
# knight

from collections import deque

dx = (-1, -2, -2, -1, 1, 2, 2, 1)
dy = (-2, -1, 1, 2, -2, -1, 1, 2)

def bfs(x, y, n):
    q = deque()
    q.append((x, y))
    cnt = 0
    
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if chess[nx][ny] == -1:
                return cnt
            if chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                cnt = chess[nx][ny]
                q.append((nx, ny))

def init_chess(n, ax, ay):
    chess = [[0] * n for _ in range(n)]
    chess[ax][ay] = -1
    
    return chess

res = []        
T = int(input())
for _ in range(T):
    n = int(input())
    x, y = map(int, input().split())
    ax, ay = map(int, input().split())
    
    if x == ax and y == ay:
        res.append(0)
        continue
    
    chess = init_chess(n, ax, ay)
    res.append(bfs(x, y, n))

for i in range(len(res)):
    print(res[i])