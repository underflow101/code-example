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
    
    
    
    
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]