n = int(input())

arr_map = [[0] * (n+1) for _ in range(n+1)]

# 사과
k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    arr_map[x][y] = -1

# input direction
l = int(input())
direction = []
for _ in range(l):
    sec, direct = input().split()
    direction.append((sec,direct))

# 게임 시작
# head set & length
arr_map[0][0] = 1
#(x,y)
snake = [[0,0]]
snake_leng = 1

#now_dir
now_dir = [1,0]

def rotation(Direct):
    # 오른쪽 x 방향
    if now_dir[0] == 1 and now_dir[1] == 0:
        # Direct == D -> 오른쪽 회전 (아래쪽 y)
        if Direct == 'D':
            now_dir[0] = 0
            now_dir[1] = 1
        # Direct == L -> 왼쪽 회전 (위 y)
        else:
            now_dir[0] = 0
            now_dir[1] = -1
    # 아래쪽 y 방향
    elif now_dir[0] == 0 and now_dir[1] == 1:
        # Direct == D -> 오른쪽 회전 (왼쪽 x)
        if Direct == 'D':
            now_dir[0] = -1
            now_dir[1] = 0
        # Direct == L -> 왼쪽 회전 (오른쪽 x)
        else:
            now_dir[0] = 1
            now_dir[1] = 0
    
    # 왼쪽 x 방향
    elif now_dir[0] == -1 and now_dir[1] == 0:
        # Direct == D -> 오른쪽 회전 (위쪽 y)
        if Direct == 'D':
            now_dir[0] = 0
            now_dir[1] = -1
        # Direct == L -> 왼쪽 회전 (아래 y)
        else:
            now_dir[0] = 0
            now_dir[1] = 1
    
    # 윗쪽 y 방향
    elif now_dir[0] == 0 and now_dir[1] == -1:
        # Direct == D -> 오른쪽 회전 (오른쪽 x)
        if Direct == 'D':
            now_dir[0] = 1
            now_dir[1] = 0
        # Direct == L -> 왼쪽 회전 (왼쪽 x)
        else:
            now_dir[0] = -1
            now_dir[1] = 0
    
    else:
        pass

def move_snake(now_dir,snake):
    # head <- body <- body .. <- tail
    # 머리 이동
    prev_for_one = [ snake[0][0], snake[0][1] ]
    snake[0][0] += now_dir[0]
    snake[0][1] += now_dir[1]
    
    # 몸통 갱신
    for i in range(1,len(snake)):
        snake[i][0] = snake[i-1][0]
        snake[i][1] = snake[i-1][1]
    
    # 실제 좌표에 갱신
    for i in range(len(snake)):
        arr_map[snake[i][1]][snake[i][0]] = 1

        if snake_leng == 1:
            arr_map[prev_for_one[1]][prev_for_one[0]] = 0
            break
        if i == len(snake) - 1:
            arr_map[snake[i][0]][snake[i][1]] = 0

sec = 0
while True:
    # 맵 범위 벗어나면
    if snake[0][0] < 0 or snake[0][0] > n or snake[0][1] < 0 or snake[0][1] > n:
        break

    # 방향 변환
    for i in direction:
        if sec == int(i[0]):
            rotation(i[1])
    # move
    move_snake(now_dir,snake)

    # 몸통에 부딫히면
    if arr_map[snake[0][1] + now_dir[0]][snake[0][0] + now_dir[1]] == 1:
        sec += 1
        break
    # 사과를 먹으면
    if arr_map[snake[0][1]][snake[0][0]] == -1:
        snake.append([snake[0][0],snake[0][1]])
        snake_leng += 1
     
    sec += 1

print(sec)
