# bead_escape
# boj 13460

from collections import deque
import sys

#input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

n, m = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
q = deque()

_rx, _ry, _bx, _by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'R':
            _rx, _ry = i, j
        elif maze[i][j] == 'B':
            _bx, _by = i, j
q.append((_rx, _ry, _bx, _by, 0))
visited[_rx][_ry][_bx][_by] = True


def move(_x, _y, _dx, _dy, _c):
    while(True):
        if maze[_x+_dx][_y+_dy] == '#' or maze[_x][_y] == 'O':
            return _x, _y, _c
        else:
            _x += _dx
            _y += _dy
            _c += 1
            
def bfs():
    while q:
        rx, ry, bx, by, c = q.popleft()
        if c > 10:
            return -1
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            
            if maze[nbx][nby] == 'O':
                continue
            if maze[nrx][nry] == 'O':
                return c + 1 if c < 10 else -1
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, c+1))
    return -1

print(bfs())