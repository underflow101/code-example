# muziMukbang.py
# book p.316

import sys
from collections import deque
from heapq import heappush, heappop
#input = sys.stdin.readline
INF = int(1e9)

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heappush(q, (food_times[i], i+1))
    sumval = 0
    prev = 0
    length = len(food_times)
    
    while sumval + ((q[0][0] - prev) * length) <= k:
        now = heappop(q)[0]
        sumval += (now - prev) * length
        length -= 1
        prev = now
    
    res = sorted(q, key=lambda x: x[1])
    return res[(k - sumval) % length][1]

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))