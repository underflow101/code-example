# findParts_bin.py
# book p.197

import sys
from collections import deque
input = sys.stdin.readline

def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    res = binarySearch(arr, i, 0, n - 1)
    if res != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')