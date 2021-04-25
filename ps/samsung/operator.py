# operator.py
# boj 14888

import sys
#input = sys.stdin.readline
sys.setrecursionlimit(100000)

max_ans = -1e19
min_ans = 1e19

n = int(input())
num = list(map(int, input().split()))
# +, -, *, //
op = list(map(int, input().split()))
op_cnt = [0] * 4

def dfs(s, c):
    global max_ans, min_ans
    if c == n:
        max_ans = max(max_ans, s)
        min_ans = min(min_ans, s)
    else:
        if op_cnt[0] != op[0]:
            ns = s + num[c]
            op_cnt[0] += 1
            dfs(ns, c+1)
            op_cnt[0] -= 1
        if op_cnt[1] != op[1]:
            ns = s - num[c]
            op_cnt[1] += 1
            dfs(ns, c+1)
            op_cnt[1] -= 1
        if op_cnt[2] != op[2]:
            ns = s * num[c]
            op_cnt[2] += 1
            dfs(ns, c+1)
            op_cnt[2] -= 1
        if op_cnt[3] != op[3]:
            ns = int(s / num[c])
            op_cnt[3] += 1
            dfs(ns, c+1)
            op_cnt[3] -= 1

dfs(num[0], 1)
print(max_ans)
print(min_ans)