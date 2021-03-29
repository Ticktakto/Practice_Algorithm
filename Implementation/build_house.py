n = int(input())
m = int(input())
build_frame = []

for _ in range(m):
    build_frame.append(list(map(int, input().split())))

def check(now_map, frame):
    x = frame[0]
    y = frame[1]
    is_pillar_or_beam = frame[2]

    # 기둥
    if is_pillar_or_beam == 0:
        # 바닥
        if y == 0:
            return True 
        # 밑에 기둥
        elif now_map[x][y-1] >= 2 and y-1 >= 0:
            return True  
        # 보
        elif x-1 >= 0 and now_map[x-1][y] == 1 or now_map[x-1][y] >= 3:
            return True
        else:
            return False
    # 보
    elif is_pillar_or_beam == 1:
        # 기둥
        if y-1 >= 0 and now_map[x][y-1] == 2:
            return True
        # 양쪽 보 사이
        elif x-1 >= 0 and x+1 < n and now_map[x-1][y] >= 1 and now_map[x+1][y] >= 1:
            return True
        else:
            return False
    else:
        return False

def solution(n, build_frame):
    now_map = [[0] * n ] * n 
    temp_map = now_map
    result = []

    for frame in build_frame:
        # now_map -> 1 => 보, 2 => 기둥, 3 => 기둥과 보의 접합부
        
        # 1이면 설치, 0이면 삭제
        x = frame[0]
        y = frame[1]
        is_pillar_or_beam = frame[2]
        is_delete_or_build = frame[3]
        can_process = True

        # temp_map 에서 기둥&보 설치 or 삭제
        if is_delete_or_build == 1:
            if is_pillar_or_beam == 0:
                temp_map[x][y] += 2
            
            elif is_pillar_or_beam == 1:
                temp_map[x][y] += 1
            
        elif is_delete_or_build == 0:
            if is_pillar_or_beam == 0:
                temp_map[x][y] -= 2
            
            elif is_pillar_or_beam == 1:
                temp_map[x][y] -= 1

        # 임시 map의 모든 기둥과 좌표에 대해 조건 체크
        for temp_x in range(n):
            for temp_y in range(n):
                temp_pillar_or_beam = temp_map[temp_x][temp_y]

                # 해당 위치가 기둥 1개
                if temp_pillar_or_beam == 2:
                    temp_frame = [temp_x,temp_y,0]
                    
                    if check(temp_map, temp_frame) == False:
                        can_process = False
                        break
                        
                # 해당 위치가 보 1개
                elif temp_pillar_or_beam == 1:
                    temp_frame = [temp_x,temp_y,1]

                    if check(temp_map, temp_frame) == False:
                        can_process = False
                        break
                # 해당 위치가 기둥 + 보
                elif temp_pillar_or_beam >= 3:
                    temp_frame_pillar = [temp_x,temp_y,0]
                    temp_frame_beam = [temp_x,temp_y,1]

                    if check(temp_map, temp_frame_pillar) == False or check(temp_map, temp_frame_beam) == False:
                        can_process = False
                        break
                
                else:
                    continue
        
        if can_process == False:
            continue
        else:
            now_map = temp_map
            result.append([x,y,is_pillar_or_beam])
    
    return result

print(solution(n,build_frame))



