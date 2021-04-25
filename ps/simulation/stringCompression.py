# stringCompression.py
# book p.323

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

def solution(s):
    ans = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ''
        prev = s[0:step]
        cnt = 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt +=1
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+step]
                cnt = 1
        compressed += str(cnt) + prev if cnt >= 2 else prev
        ans = min(ans, len(compressed))

    return ans

s = 'aabbaccccca'
print(solution(s))