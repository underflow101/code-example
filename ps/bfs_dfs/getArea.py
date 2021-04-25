# BOJ 2583
# getArea

import sys
sys.setrecursionlimit(100000)

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def dfs(x, y):
    global c
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if geo[x][y] == 1:
        geo[x][y] = 0
        c += 1
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

m, n, k = map(int, input().split())
geo = [[1] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            geo[i][j] = 0

cnt = 0
area = []
c = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
            area.append(c)
            c = 0

area.sort()
print(cnt)
for i in range(len(area)):
    print(area[i], end=' ')