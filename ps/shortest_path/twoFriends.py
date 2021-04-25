# BOJ 1058
# twoFriends

n = int(input())
visited = [[False] * n for _ in range(n)]
graph = []

for i in range(n):
    graph.append(list(map(str, input())))

def floyd_warshall():
    for k in range(n):
        for a in range(n):
            for b in range(n):
                if a == b:
                    continue
                if graph[a][b] == 'Y' or (graph[a][k] == 'Y' and graph[k][b] == 'Y'):
                    visited[a][b] = True

res = 0
floyd_warshall()

for i in range(n):
    cnt = 0
    for j in range(n):
        if visited[i][j] == True:
            cnt += 1
    res = max(res, cnt)
    
print(res)