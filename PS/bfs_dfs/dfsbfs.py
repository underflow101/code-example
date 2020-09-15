from collections import deque

ans_dfs = []
ans_bfs = []

def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))

    return visited

def BFS(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))

    return visited

n, m, v = map(int, input().split())
graph = [set([]) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

print(*DFS(graph, v))
print(*BFS(graph, v))
