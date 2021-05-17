# 8:50 ~ 9:50
from collections import deque 

n, m = map(int, input().split())

arr_map = []
for _ in range(n):
    arr_map.append(list(map(int,input())))

def dfs(arr_map):
    x, y = 0, 0
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if nx == n - 1 and ny == m - 1:
                    return arr_map[x][y] + 1

                if arr_map[nx][ny] == 1:
                    arr_map[nx][ny] = arr_map[x][y] + 1
                    queue.append((nx,ny))
    return False

res = dfs(arr_map)
print(res)

    


