# BOJ 1145
# mostlygcd

from itertools import combinations

num_input = list(map(int, input().split()))
ans = 1e9

def LCM2(i, j):
    while j != 0:
        i, j = j, i % j
    return i

def LCM3(num):
    GCD = num[0]
    LCM = num[0]
    for i in range(len(num)):
        GCD = LCM2(LCM, num[i])
        LCM = LCM * num[i] // GCD
    return LCM

for item in combinations(num_input, 3):
    ans = min(ans, LCM3(item))

print(ans)