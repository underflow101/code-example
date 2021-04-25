# BOJ 15683
# surveillance

from copy import deepcopy
import sys
sys.setrecursionlimit(100000)

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

dir = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[1, 0], [1, 2], [3, 0], [3, 2]], [[0, 1, 2], [1, 2, 3], [0, 2, 3],[0, 1, 3]], [[0, 1, 2, 3]]]

n, m = map(int, input().split())
office = []
cctv = []
total_cctv = 0

for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            total_cctv += 1
            cctv.append([i, j])
    
res = 1e9

def safe(cctv_map):
    score = 0
    for i in range(n):
        for j in range(m):
            if cctv_map[i][j] == 0:
                score += 1
    return score

def surveil(x, y, d, target_map):
    for i in d:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if target_map[nx][ny] == 0:
                    target_map[nx][ny] = 7
                elif target_map[nx][ny] == 6:
                    break
            else:
                break

def dfs(cnt, office_now):
    global res
    
    tmp = deepcopy(office_now)
    
    if cnt == total_cctv:
        res = min(res, safe(tmp))
        return
    
    x, y = cctv[cnt]
    for d in dir[office[x][y]]:
        surveil(x, y, d, tmp)
        dfs(cnt+1, tmp)
        tmp = deepcopy(office_now)

dfs(0, office)
print(res)