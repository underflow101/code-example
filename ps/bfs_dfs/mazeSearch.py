# BOJ 2178
# Maze Search

from collections import deque
import sys
#input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

def bfs(maze, n, m):
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                q.append((nx, ny))
    return maze[n-1][m-1]

n, m = map(int, input().split())
maze = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n):
    _tmp = input()
    for j in range(m):
        maze[i][j] = int(_tmp[j])

print(bfs(maze, n, m))