from collections import deque

# 노드와 간선 개수 입력
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a -> b로 연결
    indegree[b] += 1 # 진입차수 증가

def topology_sort():
    res = [] # 수행 결과를 담을 리스트
    q = deque() # Queue 초기화
    
    # 진입차수가 0인 노드를 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        res.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 결과 출력
    for i in res:
        print(i, end=' ')

topology_sort()