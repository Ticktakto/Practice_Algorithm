from collections import deque

n, m, k, x = map(int, input().split())
arr_city = [[] for i in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    arr_city[a].append(b)

# 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 위치는 0

# BFS
queue = deque([x])

while queue:
    node = queue.popleft()
    for city in arr_city[node]:
        if distance[city] == -1:
            # 최단거리 갱신
            distance[city] = distance[node] + 1
            queue.append(city)
# 최단 거리가 K인 모든 도시 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
# 만약 최단거리가 K인 도시가 없다면, False
if check == False:
    print(-1)