# BOJ 16988
# Baaaaaaaaaaduk2 (Easy)

from collections import deque
from itertools import combinations
import sys
sys.setrecursionlimit(100000)

dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
position = []
ans = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            position.append((i, j))

def bfs(x, y):
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    flag = True
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    flag = False
                elif board[nx][ny] == 2:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))
    return cnt if flag else -1

def play(pos):
    res = 0
    
    for i, j in pos:
        board[i][j] = 1
        
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2 and not visited[i][j]:
                cnt = bfs(i, j)
                if cnt != -1:
                    res += cnt
    
    for i, j in pos:
        board[i][j] = 0
    
    return res

for pos in combinations(position, 2):
    ans = max(ans, play(pos))
    visited = [[False] * m for _ in range(n)]
    
print(ans)