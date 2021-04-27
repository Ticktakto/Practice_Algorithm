# https://jjangsungwon.tistory.com/4

# visited -> bfs를 수행하면서 동적으로 cites_route가 갱신되며 계산된다
def dfs(start, next_, value, visited):
    global res

    # 시작점으로 되돌아 오는 경우
    if len(visited) == n:
        if travel[next_][start] != 0:
            res = min(res, value + travel[next_][start])
        return

    for i in range(n):
        # 다음 노드가 값이 있고, start 지점이 아니며, 아직 방문을 안 했을 경우
        if travel[next_][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next_][i], visited)
            visited.pop()

n = int(input())
travel = [list(map(int,input().split())) for _ in range(n)]

res = int(1e9)

for i in range(n):
    dfs(i, i, 0, [i])
print(res)