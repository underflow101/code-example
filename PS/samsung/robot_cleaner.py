# robot_cleaner.py
# boj 14503

from sys import stdin
# input = stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]

def turn(_d):
    nd = 4
    if _d == 0:
        nd = 3
    elif _d == 1:
        nd = 0
    elif _d == 2:
        nd = 1
    elif _d == 3:
        nd = 2
    return nd

def go_back(_d):
    nd = 4
    if _d == 0:
        nd = 2
    elif _d == 1:
        nd = 3
    elif _d == 2:
        nd = 0
    elif _d == 3:
        nd = 1
    return nd

def check(x, y, d):
    nd = d
    cnt = 4
    mp[x][y] = 2
    while cnt:
        d = nd
        cnt -= 1
        nd = turn(d)
        nx, ny = x+dx[nd], y+dy[nd]
        if mp[nx][ny] == 0:
            return nx, ny, nd, False
        else:
            continue
    return x, y, nd, True

def clean(x, y, d):
    while True:
        x, y, d, err = check(x, y, d)
        if err:
            nd = go_back(d)
            px, py = x+dx[nd], y+dy[nd]
            if mp[px][py] == 1:
                break
            else:
                x, y = px, py
                continue
        else:
            continue

clean(r, c, d)
ans = 0
for i in range(n):
    for j in range(m):
        if mp[i][j] == 2:
            ans += 1
print(ans)
