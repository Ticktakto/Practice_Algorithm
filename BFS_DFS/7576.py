# https://pacific-ocean.tistory.com/267
# 처음 토마토 위치가 여러 개인 경우 => 따로 해당 토마토 위치들을 저장하는 list 생성하여 동시에 bfs 돌릴 수 있도록 구현!

from collections import deque

m, n = map(int, input().split())

s = []
queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    s.append(list(map(int, input().split())))

def bfs():
    while queue:
        a, b = queue.popleft()
        
        for i in range(4):
            
            x = a + dx[i]
            y = b + dy[i]
            
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0:
                s[x][y] = s[a][b] + 1
                queue.append([x, y])

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])

bfs()

isTrue = False
result = -2

for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)

if isTrue == True:
    print(-1)

elif result == -1:
    # 익은 토마토들이 모두 벽으로 둘러쌓여 있는 경우(-1로 다 둘러쌓이면, 익은 토마토가 퍼질 수 없음)
    print(0)
else:
    print(result - 1)