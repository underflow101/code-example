# BOJ 16234
# movePopulation

from collections import deque
import sys
input = sys.stdin.readline

dx = (1, -1, 0, 0)
dy = (0, 0, -1, 1)

n, l, r = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def bfs(x, y):
    q = deque()
    q.append((x, y))
    unity = []
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny]:
                if l <= abs(population[x][y] - population[nx][ny]) <= r:
                    visited[nx][ny] = True
                    unity.append((nx, ny))
                    q.append((nx, ny))
    return unity
                
def calPop(unity):
    sum = 0
    for item in unity:
        sum += population[item[0]][item[1]]
    res = sum // len(unity)
    for item in unity:
        population[item[0]][item[1]] = res
    return population

while True:
    flag = False
    unity = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                unity = bfs(i, j)
                if unity:
                    flag = True
                    unity.append((i, j))
                    population = calPop(unity)
    if flag:
        cnt += 1
    else:
        break

print(cnt)