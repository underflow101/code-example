# BOJ 1014
# cheating

import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)

import sys
import re
T = int(sys.stdin.readline())
results = []

def dfs(x):
    global bimap, matched, visited
    
    if visited[x]:
        return False
    
    visited[x] = True
    for y, link in enumerate(bimap[x]):
        if link:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False

for _ in range(T):
    n, m = map(int, input().split())
    x_start = 0
    x_idx = 0
    y_start = 0
    y_idx = 0
    max = 0
    matched = {}
    sit_cnt = 0

    coord_map = []
    for _ in range(n):
        coord_map.append([0 for _ in range(m)])

    X = {}
    Y = {}
    
    bimap = []
    if m % 2 == 0:
        for _ in range(int(m/2)*n): bimap.append([0 for _ in range(int(m/2)*n)])
    else:
        for _ in range((int(m/2)+1)*n): bimap.append([0 for _ in range(int(m/2)*n)])

    for x in range(n):
        row = input().rstrip()

        turn = "X"
        x_idx = x_start
        y_idx = y_start
        for y, value in enumerate(row):
            if turn == "X":
                if value == ".":
                    X[(x, y)] = (x_idx, 1)
                    sit_cnt += 1
                else: X[(x, y)] = (x_idx, 0)
                x_idx += n
                turn = "Y"
            else:
                if value == ".":
                    Y[(x, y)] = (y_idx, 1)
                    sit_cnt += 1
                else: Y[(x, y)] = (y_idx, 0)
                y_idx += n
                turn = "X"
        x_start += 1
        y_start += 1

        for y, value in enumerate(row):
            if value == ".": coord_map[x][y] = 1

    for x, y in X:
        item = X[(x, y)]
        if not item[1]:
            continue
        candidates = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y+1), (x, y+1), (x+1, y+1)]
        for cx, cy in candidates:
            if 0 <= cx < n and 0 <= cy < m and coord_map[cx][cy]:
                bigraph_x = X[(x, y)][0]
                bigraph_y = Y[(cx, cy)][0]

                bimap[bigraph_x][bigraph_y] = 1

    for i in range(len(X)):
        visited = [False for _ in range(len(X))]
        dfs(i)
    
    result = sit_cnt - len(matched)
    results.append(result)

for result in results:
    print(str(result))