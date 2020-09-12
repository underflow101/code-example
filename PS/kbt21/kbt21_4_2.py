# kbt21_4_2
# 4. muziTaxi

from heapq import heappush, heappop
INF = int(1e9)

def solution(n, s, a, b, fares):
    ans = 0
    m = len(fares)
    graph = [[] for _ in range(n+1)]
    floydgraph = [[INF] * (n+1) for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    for i in range(m):
        j, k, w = fares[i]
        graph[j].append((k, w))
        graph[k].append((j, w))
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                floydgraph[a][b] = 0
    
    for i in range(m):
        j, k, w = fares[i]
        floydgraph[j][k] = w
        floydgraph[k][j] = w
    
    for a in range(1, n+1):
        for b in range(1, n+1):
            for j in range(1, n+1):
                for k in range(1, n+1):
                    floydgraph[j][k] = min(floydgraph[j][k], floydgraph[j][b] + floydgraph[b][k], floydgraph[j][a] + floydgraph[a][k])
    
    def dijkstra(start):
        q = []
        heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heappush(q, (cost, i[0]))
    
    dijkstra(s)
    
    dist1 = distance[a] + distance[b]
    dist2 = 
    print(dist1)
    
    
    
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

print(solution(n, s, a, b, fares))