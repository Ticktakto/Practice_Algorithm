import sys
sys.setrecursionlimit(100000)


def dfs(graph, v, visited):
    # 방문 안했으면 체크
    if visited[v] == False:
        visited[v] = True
    else:
        return False

    for node in graph[v]:
        # 자기 자신을 가리키면 -> 자체 사이클
        if node == v:
            return True    
        # dfs 수행 (True => 사이클), graph는 무조건 순회한다는 가정이라 가능!
        # https://claude-u.tistory.com/434
        if not visited[node]:
            dfs(graph, node, visited)
            return True
    return False 
        


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for i in range(n):
        a, b = i+1, arr[i]
        graph[a].append(b)
    
    count = 0
    for i in range(1,n+1):
        if dfs(graph, i, visited) == True:
            count += 1
    print(count)

    

