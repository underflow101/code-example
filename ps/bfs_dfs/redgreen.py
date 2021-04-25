# BOJ 10026
# redgreen

import sys
from copy import deepcopy
sys.setrecursionlimit(10000)

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)
dcolor = ('R', 'G', 'B')

n = int(input())
grid = []
grid_rg = []
for i in range(n):
    grid.append(list(input()))

grid_rg = deepcopy(grid)
    
res_norm = 0
res_rg = 0
    
def dfs_norm(x, y, curr):
    global n
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if grid[x][y] == curr:
        grid[x][y] = 0
        for i in range(4):
            dfs_norm(x+dx[i], y+dy[i], curr)
        return True
    return False

def dfs_rg(x, y, curr):
    global n
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if curr == 'R' or curr == 'G':
        if grid_rg[x][y] == 'R' or grid_rg[x][y] == 'G':
            grid_rg[x][y] = 0
            for i in range(4):
                dfs_rg(x+dx[i], y+dy[i], curr)
            return True
        
    if grid_rg[x][y] == curr:
        grid_rg[x][y] = 0
        for i in range(4):
            dfs_rg(x+dx[i], y+dy[i], curr)
        return True
    return False

for k in range(3):
    for i in range(n):
        for j in range(n):
            if dfs_norm(i, j, dcolor[k]):
                res_norm += 1

for k in range(3):
    for i in range(n):
        for j in range(n):
            if dfs_rg(i, j, dcolor[k]):
                res_rg += 1

print(res_norm, res_rg)