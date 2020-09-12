# kbt21_6
# 6. cardGame

from collections import deque

def solution(board, r, c):
    visited = [[False] * 4 for _ in range(4)]
    q = deque()
    dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
    visited[r][c] = True
    prev = board[r][c]
    cnt = 0
    if prev != 0:
        cnt += 1
        board[r][c] = 0
    q.append((r, c, cnt))
    
    def move(_x, _y, _dx, _dy, _c):
        while True:
            if _x+_dx < 0 or _x+_dx > 3 or _y+_dy < 0 or _y+_dy > 3:
                return _x, _y, _c
            #if board[_x+_dx][_y+_dy] != 0:
            return _x+_dx, _y+_dy, _c+1
            #else:
            #    _x += _dx
            #    _y += _dy
                
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx, ny, cnt = move(x, y, dx[i], dy[i], cnt)
            
            if board[nx][ny] == board[x][y]:
                cnt += 1
                board[nx][ny] = 0
            
            if board[x][y] == 0:
                cnt += 1
                board[nx][ny] = 0
            
            
                
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt))
                    
    return cnt

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0

print(solution(board, r, c))