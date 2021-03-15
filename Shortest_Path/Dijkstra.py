import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# node 개수, 간선 개수 입력
n, m = map(int, input().split())
# 시작 노드 입력
start = int(input())
# 각 노드 연결되어 있는 노드에 대한 정보를 담는 리스트 (그래프)
graph = [[] for i in range(n+1)] # graph => n + 1, 노드 번호 = 인덱스 처리 가능
# 최단 거리 테이블 => 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b,c)) # tuple! for heapq

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q: # queue가 빌 때 까지!
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist > distance[now]:
            continue
        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for i in graph[now]:
                cost = dist + i[1] # dist + i의 비용
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]: # distance[i의 노드 번호]
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost,i[0]))
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력 (1~n 의 인덱스 범위 = 노드 번호)
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한대를 출력
    if distance[i] == INF:
        print("INF")
    # 도달 가능한 경우, 거리를 출력
    else:
        print(distance[i])
    