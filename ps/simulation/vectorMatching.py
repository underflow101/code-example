# BOJ 1007
# vector matching

import sys
#input = sys.stdin.readline
from itertools import combinations
from math import sqrt

T = int(input())

for _ in range(T):
    n = int(input())
    coord = []
    min_sum = 1e19
    x_total, y_total = 0, 0
    
    for _ in range(n):
        x, y = map(int, input().split())
        coord.append([x, y])
        x_total += x
        y_total += y
        
    list_coord = list(combinations(coord, n//2))
    for sum_coord in list_coord[:len(list_coord)//2]:
        sum_coord = list(sum_coord)
        
        x1, y1 = 0, 0
        for dx, dy in sum_coord:
            x1, y1 = x1+dx, y1+dy

        min_sum = min(min_sum, sqrt((x1*2 - x_total)**2 + (y1*2 - y_total)**2))
    
    print(min_sum)