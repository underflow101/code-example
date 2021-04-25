# BOJ 16937
# twoStickers

import sys
from itertools import combinations
input = sys.stdin.readline

h, w = map(int, input().split())
paper = h * w
n = int(input())
stickers = []

for i in range(n):
    a, b = map(int, input().split())
    area = a * b
    stickers.append([a, b, area])
    
def flip(_sticker):
    _sticker[0], _sticker[1] = _sticker[1], _sticker[0]
    return _sticker

res = 0

for sticker in combinations(stickers, 2):
    sticker = list(sticker)
    sum_area = sticker[0][2] + sticker[1][2]
    
    for i in range(4):
        if sticker[0][0] + sticker[1][0] <= h:
            if max(sticker[0][1], sticker[1][1]) <= w:
                res = max(res, sticker[0][2] + sticker[1][2])
                break
        else:
            if sticker[0][1] + sticker[1][1] <= w:
                if max(sticker[0][0], sticker[1][0]) <= h:
                    res = max(res, sticker[0][2] + sticker[1][2])
                    break
        if i == 0:
            sticker[1] = flip(sticker[1])
        if i == 1:
            sticker[1] = flip(sticker[1])
            sticker[0] = flip(sticker[0])
        if i == 2:
            sticker[1] = flip(sticker[1])
    
print(res)