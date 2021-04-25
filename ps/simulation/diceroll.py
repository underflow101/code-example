# diceroll.py
# BOJ 14499

import sys
#input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

n, m, x, y, k = map(int, input().split())
A = [[0] * m for _ in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))

op = list(map(int, input().split()))

dice = [0] * 6
top = 0
bot = 5

for i in range(k):
    nx = x + dx[op[i]-1]
    ny = y + dy[op[i]-1]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    else:
        if op[i] == 1:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
        elif op[i] == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
        elif op[i] == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
        elif op[i] == 4:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        if A[nx][ny] == 0:
            A[nx][ny] = dice[bot]
            print(dice[top])
        else:
            dice[bot] = A[nx][ny]
            A[nx][ny] = 0
            print(dice[top])

        x, y = nx, ny
