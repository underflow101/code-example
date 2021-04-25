# examproctor.py
# BOJ 13458

import sys
#input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
b, c = map(int, input().split())

res = 0

for i in range(n):
    tmp = student[i] - b
    if tmp < 1:
        res += 1
        continue
    else:
        if tmp % c == 0:
            res += (tmp // c) + 1
        else:
            res += (tmp // c) + 2

print(res)