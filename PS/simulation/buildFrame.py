# buildFrame.py
# book p.329

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

def possible(ans):
    for x, y, stuff in ans:
        if stuff == 0:
            if y == 0 or [x-1, y-1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            return False
        elif stuff == 1:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            return False
    return True

def solution(n, build_frame):
    ans = []
    for frame in build_frame:
        x, y, stuff, op = frame
        if op == 0:
            ans.remove([x, y, stuff])
            if not possible(ans):
                ans.append([x, y, stuff])
        if op == 1:
            ans.append([x, y, stuff])
            if not possible(ans):
                ans.remove([x, y, stuff])
    return sorted(ans)