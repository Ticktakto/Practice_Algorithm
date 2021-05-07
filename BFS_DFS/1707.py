# https://it-garden.tistory.com/336
# 해당 문제는 bfs로 푸는 게 더 이해하기 쉬울 듯?
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(now, color):
    visited[now] = color
    for i in arr[now]:
        # 아직 안가본 곳이면 방문
        if visited[i] == 0:
            # 인접노드 색깔이 다른데, False 면
            if not dfs(i, -color):
                return False
        # 방문한 곳인데 색깔이 다르면 취소
        elif visited[i] == visited[now]:
            return False
    return True


for _ in range(int(input())):
    
    v, e = map(int, input().split())
    arr = [[] for _ in range(v + 1)]
    
    visited = [0] * (v + 1)
    
    for _ in range(e):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    ans = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            ans = dfs(i, 1)
            if not ans:
                break
    print("YES" if ans else "NO")


        
    

