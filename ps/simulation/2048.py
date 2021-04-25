#BOJ 12100 2048(Easy)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0
q = deque()

def get(i, j):
    if(A[i][j]):
        q.append(A[i][j])
        A[i][j] = 0
        
def merge(i, j, di, dj):
    while(q):
        x = q.popleft()
        if(not A[i][j]):
            A[i][j] = x
        elif(A[i][j] == x):
            A[i][j] = x * 2
            i, j = i + di, j + dj
        else:
            i, j = i + di, j + dj
            A[i][j] = x

def move(k):
    if(k == 0):
        for j in range(N):
            for i in range(N):
                get(i, j)
            merge(0, j, 1, 0)
    elif(k == 1):
        for j in range(N):
            for i in range(N - 1, -1, -1):
                get(i, j)
            merge(N - 1, j, -1, 0)
    elif(k == 2):
        for i in range(N):
            for j in range(N):
                get(i, j)
            merge(i, 0, 0, 1)
    else:
        for i in range(N):
            for j in range(N - 1, -1, -1):
                get(i, j)
            merge(i, N - 1, 0, -1)

def solve(cnt):
    global A, ans
    if(cnt == 5):
        for i in range(N):
            ans = max(ans, max(A[i]))
        return
    b = [x[:] for x in A]
    for k in range(4):
        move(k)
        solve(cnt + 1)
        A = [x[:] for x in b]

solve(0)
print(ans)