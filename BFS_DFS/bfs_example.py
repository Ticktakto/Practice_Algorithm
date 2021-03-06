from collections import deque

def bfs(graph, start, visited):
    
    # 시작점을 큐에 먼저 넣기
    queue = deque([start])
    visited[start] = True

    while queue:    # 큐가 빌 때 까지
        
        # 큐에서 원소 하나를 뽑아 출력
        temp = queue.popleft()
        print(temp, end=' ') 
        
        # 큐의 인접 노드에 대해
        for i in graph[temp]:
            # 한번도 방문하지 않은 노드에 대해
            if not visited[i]:
                # 인접 노드를 전부 넣고 방문 추가
                queue.append(i)
                visited[i] = True
        
        



graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)