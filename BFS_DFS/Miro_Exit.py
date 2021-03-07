from collections import deque

# 입력값 받기
n, m = map(int, input().split())

arr_map = []
for idx in range(n):
    arr_map.append(list(map(int,input())))

# 좌표 구현
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# bfs 함수 구현
def bfs():
    x = 0
    y = 0
    
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()

        for idx in range(4):
            tempX = x + dx[idx]
            tempY = y + dy[idx]

            if tempX < 0 or tempY < 0 or tempX >= n or tempY >= m:
                continue
            if arr_map[tempX][tempY] == 0:
                continue
                        
            if arr_map[tempX][tempY] == 1:
                arr_map[tempX][tempY] = arr_map[x][y] + 1
                queue.append((tempX,tempY))
                
    return arr_map[n-1][m-1]

# 알고리즘 수행
count = bfs()

# 출력
print(count)