# BOJ 2435
# weatherIntern.py

n, k = map(int, input().split())
temp = list(map(int, input().split()))
ans = -987654321

for i in range(n):
    if i+k > len(temp):
        continue
    ans = max(ans, sum(temp[i:i+k]))
print(ans)