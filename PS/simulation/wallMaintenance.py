# wallMaintenance.py
# book p.335

import sys
from collections import deque
from itertools import permutations
#input = sys.stdin.readline

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    ans = len(dist) + 1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            pos = weak[start] + friends[cnt-1]
            for idx in range(start, start + length):
                if pos < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[idx] + friends[cnt-1]
            ans = min(ans, cnt)
    if ans > len(dist):
        return -1
    return ans