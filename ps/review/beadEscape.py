# beadEscape.py

import sys
#input = sys.stdin.readline

from collections import deque

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

n, m = map(int, input().split())
A = []
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
cnt = 0

for _ in range(n):
    A.append(list(input()))

for i in range(n):
    for j in range(m):
        if A[i][j] == 'R':
            rx, ry = i, j
            A[i][j] = '.'
        elif A[i][j] == 'B':
            bx, by = i, j
            A[i][j] = '.'
q = deque()
q.append((rx, ry, bx, by, cnt))
visited[rx][ry][bx][by] = True

def pretty_print(A, rx, ry, bx, by):
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i == rx and j == ry:
                print('R', end='')
            elif i == bx and j == by:
                print('B', end='')
            else:
                print(A[i][j], end='')
        print()
            
def move(rx, ry, bx, by, cnt, i):
    while True:
        nrx, nry = rx + dx[i], ry + dy[i]
        nbx, nby = bx + dx[i], by + dy[i]
        if visited[nrx][nry][nbx][nby]:
            return rx, ry, bx, by, cnt, 0
        
        if A[nrx][nry] == 'O' and A[nbx][nby] != 'O':
            cnt += 1
            return nrx, nry, nbx, nby, cnt, 1
        elif A[nrx][nry] == '#' and A[nbx][nby] == '.':
            if A[rx][ry] == A[nbx][nby]:
                cnt += 1
                visited[rx][ry][bx][by] = True
                return rx, ry, bx, by, cnt, 0
            else:
                bx, by = nbx, nby
                visited[rx][ry][bx][by] = True
                continue
        elif A[nrx][nry] == '.' and A[nbx][nby] == '#':
            if A[nrx][nry] == A[bx][by]:
                cnt += 1
                visited[rx][ry][bx][by] = True
                return rx, ry, bx, by, cnt, 0
            else:
                rx, ry = nrx, nry
                visited[rx][ry][bx][by] = True
                continue
        elif A[nrx][nry] == '.' and A[nbx][nby] == '.':
            if A[nrx][nry] == A[nbx][nby]:
                rx, ry = nrx, nry
                visited[rx][ry][bx][by] = True
                continue
            else:    
                rx, ry = nrx, nry
                bx, by = nbx, nby
                visited[rx][ry][bx][by] = True
                continue
        elif A[nrx][nry] == '#' and A[nbx][nby] == '#':
            cnt += 1
            visited[rx][ry][bx][by] = True
            return rx, ry, bx, by, cnt, 0
        

def bfs(A):
    while q:
        rx, ry, bx, by, cnt = q.pop()
        if cnt > 10:
            return -1
        for i in range(4):
            nrx, nry, nbx, nby, cnt, state = move(rx, ry, bx, by, cnt, i)
                
            print(cnt)
            pretty_print(A, nrx, nry, nbx, nby)
            print("==================================================")
            if state:
                return cnt
            else:
                continue
        q.append((nrx, nry, nbx, nby, cnt))

print(bfs(A))