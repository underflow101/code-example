# luckyStraight_2.py
# book p.321

import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))
length = len(n)

a = sum(n[:length//2])
b = sum(n[length//2:])
if a == b:
    print("LUCKY")
else:
    print("READY")