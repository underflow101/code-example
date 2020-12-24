# BOJ 15683
# surveillance
from copy import deepcopy

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

dir = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[1, 0], [1, 3], [2, 1], [2, 3]], [[0, 1, 2], [1, 2, 3], [0, 2, 3],[0, 1, 3]], [[0, 1, 2, 3]]]

n, m = map(int, input().split())
office = []
cctv = []
tmp = [[0] * m for _ in range(n)]
total_cctv = 0

for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            total_cctv += 1
            cctv.append([i, j])
for i in range(n):
    for j in range(m):
        tmp[i][j] = office[i][j]
    
res = 1e9

def safe(tmp2):
    score = 0
    for i in range(n):
        for j in range(m):
            if tmp2[i][j] == 0:
                score += 1
    return score

def surveil(x, y, d):
    # print("d:", d)
    for i in d:
        # print("i:", i)
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = -1
                elif tmp[nx][ny] == 6:
                    break
            else:
                break  

def dfs(cnt, office_now):
    global res
    
    if cnt == total_cctv:
        tmp = deepcopy(office_now)
        res = min(res, safe(tmp))
        print("res:", res)
        return
    x, y = cctv[cnt]
    for d in dir[office[x][y]]:
        # print("dir:", dir[office[x][y]], ", d:", d)
        surveil(x, y, d)
        dfs(cnt+1, office_now)

dfs(0, office)
print(res)