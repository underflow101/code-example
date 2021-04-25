# ramp.py
# boj 14890

from sys import stdin
# input = stdin.readline

n, l = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
roads = [[0] * n for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        roads[i][j] = mp[j][i]

for i in range(n):
    roads.append(mp[i])
    
def check(r):
    global l, n
    visited = [False] * n

    for i in range(n-1):
        if r[i] == r[i+1]:
            continue
        elif r[i] - r[i+1] > 1 or r[i] - r[i+1] < -1:
            return False
        # ramp is downside
        elif r[i] - r[i+1] == 1:
            if l == 1:
                visited[i+1] = True
                continue
            else:
                for j in range(1, l):
                    if i + j + 1 >= n:
                        return False
                    if r[i+j] != r[i+j+1]:
                        return False
                for j in range(1, l+1):
                    visited[i+j] = True
                continue
        # ramp is upside
        elif r[i] - r[i+1] == -1:
            if l == 1:
                if not visited[i]:
                    visited[i] = True
                    continue
                else:
                    return False
            else:
                for j in range(1, l):
                    if i-j < 0:
                        return False
                    if r[i] != r[i-j]:
                        return False
                for j in range(l):
                    if not visited[i-j]:
                        visited[i-j] = True
                    else:
                        return False
    return True
                    
    
for road in roads:
    if check(road):
        ans += 1

print(ans)