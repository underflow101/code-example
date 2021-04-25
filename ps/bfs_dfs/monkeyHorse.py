# BOJ 1600
# monkeyHorse

from collections import deque
import sys
input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)
dx2 = (-2, -1, 1, 2, 2, 1, -1, -2)
dy2 = (1, 2, 2, 1, -1, -2, -2, -1)

k = int(input())
m, n = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, k))
    
    while q:
        x, y, c = q.popleft()
        if x == (n-1) and y == (m-1):
            return visited[x][y][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 1 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c] + 1
                q.append((nx, ny, c))
        if c > 0:
            for i in range(8):
                nx = x + dx2[i]
                ny = y + dy2[i]
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 1 and visited[nx][ny][c-1] == 0:
                    visited[nx][ny][c-1] = visited[x][y][c] + 1
                    q.append((nx, ny, c-1))
    return -1

print(bfs())