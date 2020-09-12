# kbt21_4
# 4. muziTaxi

INF = int(1e9)

def solution(n, s, a, b, fares):
    ans = 0
    m = len(fares)
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0
    
    for i in range(m):
        j, k, w = fares[i]
        graph[j][k] = w
        graph[k][j] = w
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            for j in range(1, n+1):
                for k in range(1, n+1):
                    graph[j][k] = min(graph[j][k], graph[j][b] + graph[b][k], graph[j][a] + graph[a][k])
    
    dist1 = graph[s][a] + graph[a][b]
    dist2 = graph[s][a] + graph[s][b]
    dist3 = graph[s][b] + graph[b][a]
    print(dist1, dist2, dist3)
    
    print(min(dist1, dist2, dist3))
    
    return min(dist1, dist2, dist3)
    
    
    
    
    
    
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))