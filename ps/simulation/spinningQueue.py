# BOJ 1021
# spinningQueue

from collections import deque

dx = (-1, 1)

n, m = map(int, input().split())
num = deque(map(int, input().split()))
data = []
idx = 0
cnt = 0
for i in range(1, n+1):
    data.append(i)

while num:
    if idx >= len(data):
        idx = 0
    if data[idx] == num[0]:
        data.pop(idx)
        num.popleft()
        continue
    else:
        cnt_left = 0
        cnt_right = 0
        idx_left = idx
        idx_right = idx
        while data[idx_left] != num[0]:
            cnt_left += 1
            idx_left += dx[0]
        while data[idx_right] != num[0]:
            cnt_right += 1
            idx_right += dx[1]
            if idx_right >= len(data):
                idx_right -= len(data)
        cnt += min(cnt_left, cnt_right)
        num.popleft()
        data.pop(idx_right)
        idx = idx_right

print(cnt)