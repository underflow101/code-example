# BOJ 2435
# weatherIntern.py

n, k = map(int, input().split())
temp = list(map(int, input().split()))
ans = -987654321

for m in range(1, k+1):
    for i in range(n):
        if i+m > len(temp):
            continue
        ans = max(ans, sum(temp[i:i+m]))
print(ans)