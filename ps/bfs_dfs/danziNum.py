# BOJ 2667
# danziNum

import sys

dx = (-1, 1, 0, 0)
dy = (0, 0, 1, -1)

def dfs(x, y):
    global c
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if geo[x][y] == 1:
        geo[x][y] = 0
        c += 1 
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

n = int(input())
geo = []
for i in range(n):
    geo.append(list(map(int, input())))
    
cnt = 0
house = []
c = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j):
            cnt += 1
            house.append(c)
            c = 0
            
house.sort()  
print(cnt)
for i in range(len(house)):
    print(house[i])