from collections import deque

def calc(num, P):
    res = 0
    while num != 0:
        tmp = num % 10
        res += (tmp ** P)
        num //= 10
    return res

def bfs(graph, start, visited, end):
    visited[start] = True
    queue = deque([start])
    count = 0

    while queue:
        now_ = queue.pop()

        if now_ == end:
            return count
        count += 1

        for node in graph[now_]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
        

A, P = map(int, input().split())
graph = [[] for i in range(295246)]
visited = [False] * 295246
num, answer = A, 0

while True:
    # calc
    temp = calc(num, P)

    # 만약 사이클이 만들어지면
    if temp in graph[num]:
        answer = num
        break
    # res를 graph에 갱신
    graph[num].append(temp)
    num = temp

res = bfs(graph,A,visited,answer)
print(res)




