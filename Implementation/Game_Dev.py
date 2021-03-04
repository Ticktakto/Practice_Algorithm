# 입력 받기, 이동 설정
col, row = map(int, input().split())

x, y, direction = map(int, input().split())

visit_map = [[0] * row for _ in range(col)]
visit_map[x][y] = 1

arr_map = []
for i in range(col):
    arr_map.append(list(map(int, input().split()))) 

# count 구현, 알고리즘 설계

dx = [-1,0,1,0]
dy = [0,1,0,-1]

arr_map[x][y] = 0
Your_Direction = arr_map[x][y]

count = 1
turn_point = 0

def turn_left():
    global direction
    
    if direction == 0:
        direction = 3
    else:
        direction -= 1
    
    
while True:

    turn_left()
    go_arr_map = arr_map[x + dx[direction]][y + dy[direction]]
    is_visit_map = visit_map[x + dx[direction]][y + dy[direction]]

    if go_arr_map == 0 and is_visit_map == 0 :  # 해당 direction으로 갈 수 있을 경우, 해당 위치가 0이고, 방문을 한 번도 안했을 경우!
       
        visit_map[x + dx[direction]][y + dy[direction]] = 1     # 방문함을 표시

        x = x + dx[direction]
        y = y + dy[direction]
        
        count += 1
        turn_point = 0

        continue
    
    else:
        turn_point += 1
        
        if turn_point == 4:     # 4방향 모두 못 갈 때 => 이전 칸으로 설정
            nx = x - dx[direction]
            ny = y - dy[direction]

            if arr_map[nx][ny] == 0:    # 뒤로 이동한 칸이 0일 때,
                x = nx
                y = ny
            else:       # 뒤로 이동한 칸이 1일 때 => 더 이상 좌표 갱신 불가!
                break
            turn_point = 0



# 출력
print(count)