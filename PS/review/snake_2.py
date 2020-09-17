# snake_2.py
# book p.327

from collections import deque

dir = 0
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
        
def turn(dir, c):
    if c == 'L':
        dir = (dir - 1) % 4
    elif c == 'D':
        dir = (dir + 1) % 4
    return dir
    
n = int(input())
m = int(input())
apple = []
for _ in range(m):
    apple.append(list(map(int, input().split())))

l = int(input())
turn_time = []
for _ in range(l):
    tmp = list(input().split())
    turn_time.append((int(tmp[0]), tmp[1]))

A = [[0] * (n+1) for _ in range(n+1)]

for item in apple:
    A[item[0]][item[1]] = 2

cnt = 0
x, y = 1, 1
A[x][y] = 1
snake = deque()
snake.append((x, y))
while True:
    cnt += 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 < nx <= n and 0 < ny <= n:
        if A[nx][ny] == 1:
            break
        elif A[nx][ny] == 2:
            A[nx][ny] = 1
            snake.append((nx, ny))
        elif A[nx][ny] == 0:
            A[nx][ny] = 1
            snake.append((nx, ny))
            px, py = snake.popleft()
            A[px][py] = 0
        if turn_time:
            if turn_time[0][0] == cnt:
                dir = turn(dir, turn_time[0][1])
                turn_time.pop(0)
        x = nx
        y = ny
        continue
    else:
        break
    
print(cnt)