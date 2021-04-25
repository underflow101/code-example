# BOJ 2206
# breakwalls

from collections import deque

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(2)]

def bfs(n, m):
    q = deque()
    q.append((1, 0, 0))
    visited[1][0][0] = 1
    
    while q:
        cnt, x, y = q.popleft()
        if x == n-1 and y == m-1:
            return visited[cnt][x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[cnt][nx][ny]:
                if maze[nx][ny] == 0:
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1
                    q.append((cnt, nx, ny))
                if maze[nx][ny] == 1 and cnt == 1:
                        visited[0][nx][ny] = visited[cnt][x][y] + 1
                        q.append((cnt-1, nx, ny))
    return -1

res = bfs(n, m)
print(res)