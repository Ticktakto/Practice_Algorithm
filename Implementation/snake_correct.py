n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = [] # direction info

# for apple
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# set direction input
l = int(input())
for _ in range(l):
    sec, c = input().split()
    info.append((int(sec), c))

# (동,남,서,북) 의 방향(초기화) <= 좌표 이동 관련, 이 방법이 제일 편하다! 이걸로 할 껄
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x,y = 1,1 # snake's head
    data[x][y] = 2 # is snake? => 2
    direction = 0 # 처음엔 동쪽을 보고 있음
    time = 0 # second!
    index = 0 # rotation flag
    q = [(x,y)] # snake

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # snake is in map size, 머리가 몸통에 부딫히지 않는 경우
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과 없으면, 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                # 다음 위치 갱신
                q.append((nx,ny))
                # 이전 위치
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과 존재 시, 이동 후 꼬리 그대로!
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        
        x,y = nx,ny # 실제 머리 위치 갱신
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간일 때는
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
