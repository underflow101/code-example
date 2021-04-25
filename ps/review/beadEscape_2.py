#구슬탈출2

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
A = [list(input().strip()) for _ in range(n)]
visit = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
q = deque()

def init():
    _rx, _ry, _bx, _by = [0] * 4
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'R':
                _rx, _ry = i, j
            if A[i][j] == 'B':
                _bx, _by = i, j
    q.append((_rx, _ry, _bx, _by, 0))
    visit[_rx][_ry][_bx][_by] = True
    
def move(_x, _y, _dx, _dy, _c):
    while True:
        if A[_x+_dx][_y+_dy] == '#' or A[_x][_y] == 'O':
            return _x, _y, _c
        else:
            _x += _dx
            _y += _dy
            _c += 1

def bfs():
    while q:
        rx, ry, bx, by, d = q.popleft()
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            
            if A[nbx][nby] == 'O':
                continue
            if A[nrx][nry] == 'O':
                print(d+1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visit[nrx][nry][nbx][nby]:
                visit[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d+1))
    print(-1)
    
init()
bfs()