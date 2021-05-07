from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

# vertex 번호가 작은 순대로 방문 => 정렬
for idx in range(1,n+1):
    graph[idx].sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

# dfs
def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True

    print(v, end=' ')

    for node in graph[v]:
        if not visited_dfs[node]:
            dfs(graph, node, visited_dfs)

# bfs
def bfs(graph, start, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        node = queue.popleft()
        
        print(node, end=' ')
        
        for v in graph[node]:
            if not visited_bfs[v]:
                queue.append(v)
                visited_bfs[v] = True 

dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)