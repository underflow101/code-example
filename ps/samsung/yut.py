# yut.py
# boj 17825

import sys
# input = sys.stdin.readline
sys.setrecursionlimit(1000000)

op = list(map(int, input().split()))
mp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21, 23, 24, 30, 26, 30, 28, 29,
      30, 31, 32, 20]
jmp = [0] * 33
jmp[5], jmp[10], jmp[15] = 22, 25, 27
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 22, 24, 28,
         27, 26, 25, 30, 35]
player = [0, 0, 0, 0]
visited = [False] * 33
ans = 0

def dfs(idx, s):
    global ans
    if idx == 10:
        ans = max(ans, s)
        return
    for i in range(4):
        src, dst, _op = player[i], player[i], op[idx]
        
        if jmp[dst]:
            dst = jmp[dst]
            _op -= 1
        if dst + _op <= 21:
            dst += _op
        else:
            for _ in range(_op):
                dst = mp[dst]

        if visited[dst] and dst != 21:
            continue
        
        visited[src], visited[dst], player[i] = False, True, dst
        dfs(idx+1, s+score[dst])
        visited[src], visited[dst], player[i] = True, False, src

dfs(0, 0)
print(ans)
        