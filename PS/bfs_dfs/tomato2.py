# BOJ 7569
# tomato2

from collections import deque

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
dl = (-1, 1)

m, n, h = map(int, input().split())
box = [[] for _ in range(h)]

for i in range(h):
    for _ in range(n):
        box[i].append(list(map(int, input().split())))

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))

def check(m, n, h):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return False
    return True

def bfs(q, m, n, h):
    if check(m, n, h):
        return 1
    
    tmp = 0
    while q:
        l, x, y = q.popleft()
        for i in range(2):
            nl = l + dl[i]
            
            if nl < 0 or nl >= h:
                continue
            if box[nl][x][y] == -1:
                continue
            if box[nl][x][y] == 0:
                box[nl][x][y] = box[l][x][y] + 1
                tmp = box[nl][x][y]
                q.append((nl, x, y))
                
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if box[l][nx][ny] == -1:
                continue
            if box[l][nx][ny] == 0:
                box[l][nx][ny] = box[l][x][y] + 1
                tmp = box[l][nx][ny]
                q.append((l, nx, ny))
    
    if check(m, n, h):
        return tmp
    else:
        return 0
    
print(bfs(q, m, n, h)-1)