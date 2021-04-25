# lyricFind.py
# book p.370

import sys
from collections import deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
#input = sys.stdin.readline
INF = int(1e9)

def count_by_range(a, l_val, r_val):
    r_idx = bisect_right(a, r_val)
    l_idx = bisect_left(a, l_val)
    return r_idx - l_idx

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    ans = []
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()
    
    for q in queries:
        if q[0] != '?':
            res = count_by_range(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        ans.append(res)
    return ans

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))