import sys
sys.setrecursionlimit(10000) # 재귀 허용깊이 임의로 지정

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(graph, v, visited):    
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, visited)
            

for i in range(1,n+1):

    if not visited[i]:
        dfs(graph,i,visited)
        count += 1
print(count)




    