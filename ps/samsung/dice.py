# dice.py
# boj 14499

from sys import stdin
from collections import deque

#input = stdin.readline

dx = (0, 0, -1, 1)
dy = (1, -1, 0, 0)

n, m, x, y, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
op = deque(map(int, input().split()))
dice = [0] * 6

def check():
    if A[x][y] == 0:
        A[x][y] = dice[5]
    else:
        dice[5] = A[x][y]
        A[x][y] = 0

while op:
    _op = op.popleft() - 1
    if x+dx[_op] < 0 or x+dx[_op] >= n or y+dy[_op] < 0 or y+dy[_op] >= m:
        continue
    else:
        if _op == 0:
            dice[0], dice[2], dice[5], dice[3] = dice[3], dice[0], dice[2], dice[5]
            x, y = x+dx[_op], y+dy[_op]
            check()
        elif _op == 1:
            dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]
            x, y = x+dx[_op], y+dy[_op]
            check()
        elif _op == 2:
            dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0]
            x, y = x+dx[_op], y+dy[_op]
            check()
        elif _op == 3:
            dice[0], dice[4], dice[5], dice[1] = dice[1], dice[0], dice[4], dice[5]
            x, y = x+dx[_op], y+dy[_op]
            check()
        print(dice[0])