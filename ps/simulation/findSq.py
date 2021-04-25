# BOJ 1025
# Find Square

from math import sqrt

n, m = map(int, input().split())
num = []
for i in range(n):
    num.append(list(map(int, input())))

res = -1

for i in range(n):
    for j in range(m):
        for dx in range(-n, n):
            for dy in range(-m, m):
                if dx == 0 and dy == 0:
                    continue
                idx = 0
                x = i
                y = j
                tmp = ""
                while 0 <= x < n and 0 <= y < m:
                    tmp += str(num[x][y])
                    val = sqrt(int(tmp))
                    if val == int(val):
                        res = max(res, int(val)**2)
                    x += dx
                    y += dy
                    
print(res)