# https://developmentdiary.tistory.com/437?category=847525
# DFS in Tree (임의의 노드x에 대해 DFS(x)에서의 최장거리를 이루는 y를 구하고 DFS(y)를 구해 최장 길이를 구하면 노드의 지름을 구할수 있다.)
import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    par, chi, val = map(int, input().split())
    arr[par].append([chi, val])
    arr[chi].append([par, val])

# 첫 DFS (단순히 최장 경로 노드를 구하기 위한 작업)
res1 = [0 for _ in range(n+1)]

def dfs(arr, start, res):
    for node, val in arr[start]:
        if res[node] == 0:
            res[node] = res[start] + val
            dfs(arr, node, res)

# 아무 노드나 출발시켜 준다 (루트를 모르므로, 총 dfs는 2번 돌린다)
dfs(arr, 1, res1)
res1[1] = 0

max_, longest_node = 0, 0 # 최장 경로 노드를 구한다
for i in range(len(res1)):
    if max_ < res1[i]:
        max_ = res1[i]
        longest_node = i # 가장 큰 값 => 특정 노드에서 가장 멀리까지 갔음을 의미한다
# 값이 클수록, 제일 멀리 or 값이 큰 간선을 모두 거쳤다고 의미한다. => 특정 노드에 상관없이 최장 경로 노드가 구해진다. 

res2 = [0 for _ in range(n+1)] # 최장 경로 노드에서 다시 dfs 수행 => 해당 값이 트리의 지름
dfs(arr, longest_node, res2)
res2[longest_node] = 0
print(max(res2))







