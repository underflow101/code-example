# BOJ 1420
# DontGoSchool

n, m = map(int, input().split())
data = []
tmp = [['.'] * m for _ in range(n)]
wall = 0

for _ in range(n):
    data.append(list(input()))

for i in range(n):
    for j in range(m):
        if data[i][j] == 'K':
            k1, k2 = i, j
        if data[i][j] == '#':
            wall += 1

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

res = 0
flag = False

def dfs_man(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tmp[nx][ny] == '.':
                tmp[nx][ny] = '#'
                dfs_man(nx, ny)
                if tmp[nx][ny] == 'H':
                    return False
    return True
                
def exception(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 'H' or data[x][y] == 'H':
                return -1
    return 1

def safe():
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == '.':
                score += 1
    return score

def dfs(cnt):
    global res, k1, k2, flag

    if flag:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = data[i][j]
        if dfs_man(k1, k2):
            res = max(res, safe())
            print("res =", res)
        return
        
    for i in range(n):
        for j in range(m):
            flag = True
            if data[i][j] == '.':
                data[i][j] = '#'
                cnt += 1
                dfs(cnt)
                data[i][j] = '.'
                cnt -= 1
                
if exception(k1, k2) == -1:
    print(-1)
else:
    dfs(0)
    print((n*m) - res - wall - 2)