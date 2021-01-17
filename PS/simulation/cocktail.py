# BOJ 1033
# cocktail

from math import gcd
from collections import deque

n = int(input())
ing = [1] * n
matrix = [[0] * n for _ in range(n)]
a = [0] * n
b = [0] * n
p = [0] * n
q = [0] * n

for i in range(n-1):
    _a, _b, _p, _q = map(int, input().split())
    a[i] = _a
    b[i] = _b
    p[i] = _p
    q[i] = _q
    matrix[a[i]].append(b[i])
    matrix[b[i]].append(a[i])
    
def bfs(start, ban, k):
    visited = [False] * n
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        curr = queue.popleft()
        if curr == ban:
            continue
        ing[curr] *= k
        for item in matrix[curr]:
            if not visited[item]:
                queue.append(item)
                visited[item] = True
                
for i in range(n-1):
    bfs(a[i], b[i], p[i])
    bfs(b[i], a[i], q[i])
    
mult = ing[0]
for i in range(1, n):
    mult = gcd(mult, ing[i])

for i in range(n):
    print(ing[i] // mult, end=' ')