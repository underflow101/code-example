# BOJ 1033
# cocktail

n = int(input())
ing = [[0] * n for _ in range(n)]

for i in range(n-1):
    a, b, p, q = map(int, input().split())
    ing[a][b] = p / q
    ing[b][a] = q / p

for i in range(n):
    print(ing[i])
