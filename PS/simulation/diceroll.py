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
now = 0

def top(dice, now):
    if now > 1:
        return dice[now-2]
    else:
        return dice[now+2]

for i in range(k):
    nx = x + dx[op[i]-1]
    ny = y + dy[op[i]-1]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    else:
        if op[i] == 1:
            