# BOJ 4458
# uppercase

T = int(input())
for _ in range(T):
    res = str(input().rstrip())
    print(res[0].upper() + res[1:])