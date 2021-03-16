import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance =[INF] * (n+1)

# input all edge
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

# dijkstra (외우기!)
def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

# get max distance

city_num = 0
max_dist = 0

for i in distance:
    if i != INF:
        city_num += 1
        max_dist = max(max_dist, i)

print(city_num - 1, max_dist)