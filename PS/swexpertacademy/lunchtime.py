# lunchtime.py
# Samsung SW Expert Academy
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5-BEE6AK0DFAVl

from collections import deque

T = int(input())
real_ans = []
for _ in range(T):
    n = int(input())

    room = []
    for _ in range(n):
        room.append(list(map(int, input().split())))

    # person: (x, y, s_choice, time)
    p = []

    # stair: (x, y, k, cnt)
    s = []

    for i in range(n):
        for j in range(n):
            if room[i][j] == 1:
                p.append([i, j, 0, 0])
            elif room[i][j] > 1:
                s.append([i, j, room[i][j], 0])

    for i in range(len(p)):
        tmp = []
        for j in range(len(s)):
            dist = abs(p[i][0] - s[j][0]) + abs(p[i][1] - s[j][1])
            tmp.append((j, dist))
        if tmp[0][1] > tmp[1][1]:
            res = tmp[1][0]
        else:
            res = tmp[0][0]
        p[i][2] = tmp[res][0]
        p[i][3] = tmp[res][1]

    ans = 0
    s1 = deque()
    s2 = deque()
    for i in range(len(p)):
        if p[i][2] == 0:
            s1.append(p[i])
        else:
            s2.append(p[i])
    s1 = deque(sorted(s1, key=lambda x: x[3]))
    s2 = deque(sorted(s2, key=lambda x: x[3]))
    
    time1 = 0
    stair1 = s[0][2]
    cnt = 0
    prev = 0
    now = 0
    ptmp = deque()
    while s1:
        tmp = s1.popleft()
        cnt += 1
        now = tmp[3] + stair1 + 1
        prev = tmp[3]
        if cnt > 3:
            if now - ptmp[0] <= 0:
                cnt -= 1
                ptmp.popleft()
            else:
                now += now - ptmp[0]
                ptmp.popleft()
                cnt -= 1
        ptmp.append(now)
    time1 = now

    time2 = 0
    stair2 = s[1][2]
    cnt = 0
    prev = 0
    now = 0
    ptmp = deque()
    while s2:
        tmp = s2.popleft()
        cnt += 1
        now = tmp[3] + stair2 + 1
        prev = tmp[3]
        if cnt > 3:
            if now - ptmp[0] <= 0:
                cnt -= 1
                ptmp.popleft()
            else:
                now += now - ptmp[0]
                ptmp.popleft()
                cnt -= 1
        ptmp.append(now)
    time2 = now
    
    real_ans.append(max(time1, time2))

for i in range(1, len(real_ans)+1):
    print("#", end='')
    print(i, real_ans[i-1])
    