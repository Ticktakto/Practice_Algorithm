def possible(answer):
    for x, y, stuff in answer:
        
        if stuff == 0: # 설치한 것이 기둥인 경우
            # 바닥 위 or 보의 한 쪽 끝부분 위 or 다른 기둥 위 면 정상
            if y == 0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False

        elif stuff == 1: # 설치한 것이 보인 경우
            # 한쪽 끝 부분이 기둥 위 혹은 양쪽 끝 부분이 보와 동시에 연결인 경우면 정상
            if [x, y-1, 0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True
            


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        if operate == 0:# 삭제
            # 일단 삭제해보고,
            answer.remove([x,y,stuff])

            if not possible(answer): # 가능한지 test
                answer.append([x,y,stuff]) # 못하면 다시 추가

        if operate == 1:# 설치
                answer.append([x,y,stuff])

                if not possible(answer):
                    answer.remove([x,y,stuff])
        
        return sorted(answer)