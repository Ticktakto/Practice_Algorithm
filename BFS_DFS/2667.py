# 8:13 ~ 9:13
from collections import deque

def bfs(arr_map, x, y):
    n = len(arr_map)
    queue = deque()
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    if arr_map[x][y] == 0:
        return 0
    
    arr_map[x][y] = 0
    queue.append([x,y])
    count = 1

    while queue:
        now_ = queue.popleft()

        for i in range(4):
            nx = now_[0] + dx[i]
            ny = now_[1] + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= n:
                continue  
            
            if arr_map[nx][ny] == 1:
                arr_map[nx][ny] = 0
                queue.append([nx,ny])
                count += 1
    
    return count

n = int(input())
arr_map = []

for _ in range(n):
    arr_map.append(list(map(int,input())))

res = []

for x in range(n):
    for y in range(n):
        ans = bfs(arr_map, x, y)
        if ans >= 1:
                        
            res.append(ans)
res.sort()
print(len(res))
for i in res:
    print(i)
        

