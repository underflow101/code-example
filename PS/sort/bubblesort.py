# BOJ 1517
# bubblesort

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000000)

n = int(input())
num = list(map(int, input().split()))
swap = 0
 
def merge_sort(start, end):
    global swap, num
    size = end - start
    mid = (start + end) // 2
    if size <= 1:
        return
 
    merge_sort(start, mid)
    merge_sort(mid, end)
 
    tmp = []
    idx1, idx2 = start, mid
    cnt = 0
    while idx1 < mid and idx2 < end:
        if num[idx1] > num[idx2]:
            tmp.append(num[idx2])
            idx2 += 1
            cnt += 1
        else:
            tmp.append(num[idx1])
            idx1 += 1
            swap += cnt
    
    while idx1 < mid:
        tmp.append(num[idx1])
        idx1 += 1
        swap += cnt
    while idx2 < mid:
        tmp.append(num[idx2])
        idx2 += 1
    
    for t in range(len(tmp)):
        num[start + t] = tmp[t]
 
merge_sort(0, n)
print(swap)