from collections import deque
import copy # For Deep Copy!

n = int(input())

graph = [[] for i in range(n+1)] # 인접 리스트
indegree = [0] * (n+1)
time = [0] * (n+1)

for i in range(1,n+1):
    input_data = list(map(int,input().split()))
    time[i] = input_data[0]

    for x in input_data[1:-1]: # (선행 과목 번호들), -1
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    res = copy.deepcopy(time) # time의 값들을 전부 복사
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()

        for i in graph[now]:
            res[i] = max(res[i], time[i] + res[now])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1,n+1):
        print(res[i])

topology_sort()
