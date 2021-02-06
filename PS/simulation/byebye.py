# BOJ 1535
# byebye

from itertools import combinations

n = int(input())
hp = list(map(int, input().split()))
happiness = list(map(int, input().split()))
ttl = []
ans = []

for i in range(n):
    ttl.append([hp[i], happiness[i]])

for i in range(n, -1, -1):
    for tmp in combinations(ttl, i):
        q = list(tmp)
        sum_hp = 0
        sum_hap = 0
        for j in range(len(q)):
            sum_hp += q[j][0]
            sum_hap += q[j][1]
        if sum_hp >= 100:
            continue
        else:
            ans.append(sum_hap)

print(max(ans))