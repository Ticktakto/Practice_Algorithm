# https://claude-u.tistory.com/192
# python3은 시간 초과! -> visited 사용해서 시간복잡도가 n임..

from collections import deque

n = int(input())
arr = [[] for _ in range(n+1)]
visited = [False ] * (n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(visited, arr, start):
    queue = deque()
    
    parent = [0] * (n+1)
    for child in arr[start]:
        parent[child] = start
    queue.append(arr[start])
    visited[start] = True

    while queue:
        childs = queue.popleft()

        for child in childs:
            if not visited[child]:
                visited[child] = True

                for i in arr[child]:
                    if parent[i] == 0 and visited[i] == False:
                        parent[i] = child
                queue.append(arr[child])
    return parent

res = dfs(visited, arr, 1)
for i in range(2,n+1):
    print(res[i])



