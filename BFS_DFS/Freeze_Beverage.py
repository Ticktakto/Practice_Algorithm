
# 인풋 선언
n, m = map(int, input().split())

arr_map = []
for i in range(n):
    arr_map.append(list(map(int, input())))

# dfs
def dfs(x,y):
    # 종료 조건 => 맵의 범위를 벗어날 때
    if x <= -1 or y <= -1 or x >= n or y >= m :
        return False
    
    if arr_map[x][y] == 0:  # 방문하지 않은 노드에 대해 ( 여기 scope에 들어온 순간 True! )
        
        arr_map[x][y] = 1   # 방문했다고, visited 처리
        
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        
        return True
    return False


    
res = 0

# 출력
for c in range(n):
    for r in range(m):
        if dfs(c, r) == True:   # True => 현재 위치에서 0 = True -> 재귀적으로 0 = True 아니면 False .. ( 0 집단 )
            res += 1

print(res)        