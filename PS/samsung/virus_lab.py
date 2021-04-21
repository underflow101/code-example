# virus_lab.py
# boj 14502

import sys
# input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
_mp = [[0] * m for _ in range(n)]
virus = []
ans = 0

for i in range(n):
    for j in range(m):
        if mp[i][j] == 2:
            virus.append([i, j])

def safe():
    sf = 0
    for i in range(n):
        for j in range(m):
            if _mp[i][j] == 0:
                sf += 1
    return sf

def dfs_virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if _mp[nx][ny] == 0:
                _mp[nx][ny] = 2
                dfs_virus(nx, ny)

def dfs_wall(cnt):
    global ans
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                _mp[i][j] = mp[i][j]
        for item in virus:
            dfs_virus(item[0], item[1])
        ans = max(ans, safe())
        return
    else:
        for i in range(n):
            for j in range(m):
                if mp[i][j] == 0:
                    cnt += 1
                    mp[i][j] = 1
                    dfs_wall(cnt)
                    mp[i][j] = 0
                    cnt -= 1

dfs_wall(0)
print(ans)
