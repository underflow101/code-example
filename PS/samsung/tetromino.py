# tetromino.py
# boj 14500

import sys
sys.setrecursionlimit(100000)
#input = sys.stdin.readline

A = [[[1, 1, 1, 1]], [[1], [1], [1], [1]]]
B = [[[1, 1], [1, 1]]]
C = [[[1, 0], [1, 0], [1, 1]], [[1, 1, 1], [1, 0, 0]], [[1, 1], [0, 1], [0, 1]], [[0, 0, 1], [1, 1, 1]],
     [[0, 1], [0, 1], [1, 1]], [[1, 0, 0], [1, 1, 1]], [[1, 1], [1, 0], [1, 0]], [[1, 1, 1], [0, 0, 1]]]
D = [[[1, 0], [1, 1], [0, 1]], [[0, 1, 1], [1, 1, 0]], [[0, 1], [1, 1], [1, 0]], [[1, 1, 0], [0, 1, 1]]]
E = [[[1, 1, 1], [0, 1, 0]], [[0, 1], [1, 1], [0, 1]], [[0, 1, 0], [1, 1, 1]], [[1, 0], [1, 1], [1, 0]]]

tetro = [A, B, C, D, E]

n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for items in tetro:
    for item in items:
        for i in range(n):
            for j in range(m):
                res = 0
                if (len(item) + i) > n or (len(item[0]) + j) > m:
                    continue
                else:
                    for k in range(len(item)):
                        for v in range(len(item[0])):
                            res += (item[k][v] * mp[i+k][j+v])
                ans = max(ans, res)

print(ans)