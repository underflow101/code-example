# run.py
# boj 14501

import sys
# input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
mp = []

for i in range(n):
    _day, _cost = map(int, input().split())
    mp.append([_day+i, _cost])

def dfs(day, cost):
    global ans
    ans = max(ans, cost)
    if day == n:
        return ans
    
    dfs(day+1, cost)
    if mp[day][0] <= n:
        cost += mp[day][1]
        dfs(mp[day][0], cost)
    return False

ans = 0
cost = dfs(0, 0)

print(ans)