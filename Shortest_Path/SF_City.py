n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1) ]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    # 간선의 방향은 고려하지 않는다.
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# Floyd - Warshall 
for k in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

res = graph[1][k] + graph[k][x] # 1번 노드 -> k번 노드 방문, k번 노드 -> x번 노드 방문 (둘 다 최단) 

if res >= INF:
    print(-1)
else:
    print(res)