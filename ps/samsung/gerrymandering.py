# gerrymandering.py
# boj 17779

from sys import stdin
# input = stdin.readline

n = int(input())
mp = [list(map(int, input().split())) for _ in range(n)]
x, y, d1, d2 = 1, 1, 1, 1
ans = 1e19
total = 0
for i in range(n):
    total += sum(mp[i])

def gerry(x, y, d1, d2, res):
    while True:
        while True:
            lx, rx, ly, ry, bx, by = x+d1, x+d2, y-d1, y+d2, x+d1+d2, y-d1+d2
            if rx == n-1 or ry == n:
                break
            if bx >= n or by >= n or by < 0:
                break
            res = min(res, check(x, y, lx, rx, ly, ry, bx, by))
            d2 += 1
        d1 += 1
        if x+d1 == n-1 or y-d1 == -1:
            break
        d2 = 1
    return res

def check(x, y, lx, rx, ly, ry, bx, by):
    a, b, c, d, e = 0, 0, 0, 0, 0
    dir = 0
    for i in range(lx):
        for j in range(y+1):
            if [i, j] == [x+dir, y-dir]:
                dir += 1
                break
            a += mp[i][j]
    dir = 1
    for i in range(rx+1):
        for j in range(n-1, y, -1):
            if [i, j] == [x+dir, y+dir]:
                dir += 1
                break
            b += mp[i][j]
    dir = 0
    for i in range(lx, n):
        for j in range(by):
            if [i, j] == [lx+dir, ly+dir]:
                dir += 1
                break
            c += mp[i][j]
    dir = 1
    for i in range(rx+1, n):
        for j in range(n-1, by-1, -1):
            if [i, j] == [rx+dir, ry-dir]:
                dir += 1
                break
            d += mp[i][j]
    e = total - a - b - c - d
    max_pop = max(a, b, c, d, e)
    min_pop = min(a, b, c, d, e)
    return max_pop - min_pop

for i in range(n-2):
    for j in range(1, n-1):
        x, y = i, j
        d1, d2 = 1, 1
        ans = gerry(x, y, d1, d2, ans)

print(ans)