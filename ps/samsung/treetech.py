# treetech.py
# boj 16235

from sys import stdin
# input = stdin.readline

dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

n, m, k = map(int, input().split())
mp = [[5] * n for _ in range(n)]
fert = [list(map(int, input().split())) for _ in range(n)]
tree = list()

for _ in range(m):
    _x, _y, _z = map(int, input().split())
    # x, y, yo
    tree.append([_x-1, _y-1, _z])

for i in range(k):
    tree = sorted(tree, key=lambda x:(x[0], x[1], x[2]))
    
    # spring & summer
    tmp = list()
    dead = list()
    for item in tree:
        if mp[item[0]][item[1]] < item[2]:
            mp[item[0]][item[1]] += (item[2] // 2)
        else:
            mp[item[0]][item[1]] -= item[2]
            tmp.append([item[0], item[1], item[2] + 1])
    tree = list(tmp)
    
    # fall
    for items in tree:
        if items[2] % 5 == 0:
            for i in range(8):
                if 0 <= items[0]+dx[i] < n and 0 <= items[1]+dy[i] < n:
                    tree.append([items[0]+dx[i], items[1]+dy[i], 1])
    
    # winter
    for i in range(n):
        for j in range(n):
            mp[i][j] += fert[i][j]
            
print(len(tree))