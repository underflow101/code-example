# BOJ 7576
# tomato

from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

m, n = map(int, input().split())
box = []

for _ in range(n):
    box.append(list(map(int, input().split())))
    
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))
            
def check():
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == 0:
                return False
    return True

def bfs(q):
    if check():
        return 1
    
    tmp = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if box[nx][ny] == -1:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                tmp = box[nx][ny]
                q.append((nx, ny))
    
    if check():
        return tmp
    else:
        return 0
    
print(bfs(q)-1)