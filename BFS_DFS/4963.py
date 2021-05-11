import sys
sys.setrecursionlimit(10 ** 6)

#dx = [-1,0,1,0]
#dy = [0,-1,0,1]

def dfs(arr_map, x, y):
    w, h = len(arr_map[0]), len(arr_map)
    
    if x < 0 or x >= h or y < 0 or y >= w: 
        return False
    elif arr_map[x][y] == 0:
        return False
    
    elif arr_map[x][y] == 1:
        arr_map[x][y] = 0
        dfs(arr_map, x-1, y)
        dfs(arr_map, x-1, y+1)
        dfs(arr_map, x-1, y-1)
        
        dfs(arr_map, x+1, y)
        dfs(arr_map, x+1, y-1)
        dfs(arr_map, x+1, y+1)

        dfs(arr_map, x, y-1)
        dfs(arr_map, x, y+1)

        return True    


while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    arr_map = []
    for _ in range(h):
        arr_map.append(list(map(int, input().split())))
    
    res = 0
    for x in range(h):
        for y in range(w):
            if dfs(arr_map, x, y):
                res += 1
    
    print(res)

    
