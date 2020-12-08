# BOJ 1012
# cabbage.py

import sys
sys.setrecursionlimit(10000) 

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
cnt = 0
res = []

def dfs(x, y, n, m):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if geo[x][y] == 1:
        geo[x][y] = 0
        for i in range(4):
            dfs(x+dx[i], y+dy[i], n, m)
        return True
    return False

def init_geo(geo, k): 
    for _ in range(k):
        y, x = map(int, input().split())
        geo[x][y] = 1
    
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    cnt = 0
    geo = [[0] * m for _ in range(n)]
    
    init_geo(geo, k)
    
    for i in range(n):
        for j in range(m):
            if dfs(i, j, n, m):
                cnt += 1
    
    res.append(cnt)

for i in range(len(res)):
    print(res[i])
