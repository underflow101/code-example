# BOJ 1028
# diamondmine.py

from collections import deque
import sys
input = sys.stdin.readline

dy = (-1, 1)

r, c = map(int, input().split())
mine = []
for _ in range(r):
    mine.append(list(input().strip()))
max_level = round((min(r,c)+0.1) / 2)
tmp = 0

def check(lvl, x, y, r, c):
    remain_x = r - x
    remain_y = c - y
    if remain_x < lvl or y+1 < lvl or remain_y < lvl:
        return False
    else:
        return True

def get_size(level):
    if level == 1:
        return 1
    else:
        return 4 * (level-1)
    
def bfs(x, y, r, c, lvl):
    global tmp, max_level
    q = deque()
    q.append((x, y))
    tmp_level = 0
    flag = False
    
    while q:
        x, y = q.popleft()
        for i in range(2):
            if not flag:
                nx = x + 1
                ny = y + dy[i]
            else:
                nx = x + 1
                ny = y - dy[i]
            
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return False
            if mine[nx][ny] == '0':
                return False
            if mine[nx][ny] == '1':
                tmp += 1
                q.append((nx, ny))
        tmp_level += 1
        if tmp_level == lvl - 1:
            flag = True
    return True

res = []
res.append(0)

for i in range(r):
    for j in range(c):
        if mine[i][j] == '1':
            for k in range(max_level, 0, -1):
                if not check(k, i, j, r, c):
                    continue
                tmp = 0
                bfs(i, j, r, c, k)
                if tmp+1 == get_size(k):
                    res.append(k)

print(max(res))