# exam_director.py
# boj 13458

from sys import stdin
from math import ceil

#input = stdin.readline

n = int(input())
room = list(map(int, input().split()))
main, sub = map(int, input().split())
ans = 0

ans += n

for i in range(n):
    tmp = room[i] - main
    if tmp > 0:
        ans += ceil(tmp / sub)
        

print(int(ans))