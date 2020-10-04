# labvirus.py
# BOJ 14502
# Book p.341

n, m = map(int, input().split())
data = []
tmp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

res = 0

def dfs_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
        #if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                dfs_virus(nx, ny)
                
def safe():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                score += 1
    return score

def dfs(cnt):
    global res
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    dfs_virus(i, j)
        res = max(res, safe())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                cnt += 1
                dfs(cnt)
                data[i][j] = 0
                cnt -= 1

dfs(0)
print(res)