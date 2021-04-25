# Number of islands
# p. 334
# BOJ 4963

import sys
sys.setrecursionlimit(10000) 

dx = (1, -1, 0, 0, 1, -1, 1, -1)
dy = (0, 0, 1, -1, 1, -1, -1, 1)

def numisland(grid) -> int:
    def dfs(i, j):
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != 1:
                return

        grid[i][j] = 0
        for x in range(8):
            nx = i + dx[x]
            ny = j + dy[x]
            dfs(nx, ny)
    
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                cnt += 1
    return cnt

res = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        grid = []
        for i in range(h):
            grid.append(list(map(int, input().split())))
        res.append(numisland(grid))

for i in range(len(res)):
    print(res[i])