# binarysearch.py
# book p.190

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

n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

res = binarySearch(arr, target, 0, n - 1)
if res == None:
    print("Element doesn't exist!")
else:
    print(res + 1)