# keysAndLocks_2.py
# book p.325

import sys
#input = sys.stdin.readline
from collections import deque

def rotMat(key):
    n = len(key)
    rotkey = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotkey[i][j] = key[n-j-1][i]
    return rotkey

def check(lock):
    n = len(lock) // 3
    for i in range(n, n*2):
        for j in range(n, n*2):
            if lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(key)
    m = len(lock)
    length = 3*m
    newlock = [[0] * length for _ in range(length)]
    
    for i in range(m):
        for j in range(m):
            newlock[i+m][j+m] = lock[i][j]
    
    for _ in range(4):
        key = rotMat(key)
        for i in range(m*2):
            for j in range(m*2):
                for k in range(n):
                    for v in range(n):
                        newlock[i+k][j+v] += key[k][v]
                if check(newlock):
                    return True
                for k in range(n):
                    for v in range(n):
                        newlock[i+k][j+v] -= key[k][v]
    return False                
    
    
    
    
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))