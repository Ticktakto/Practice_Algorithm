# 징검다리 건너기 (https://programmers.co.kr/learn/courses/30/lessons/64062)
# 8:30 ~ 9:30
# https://hazung.tistory.com/105

stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3

def check(mid, stones, k):
    
    ck = 0
    # 돌 - 건넌 친구의 수 == > 해당 친구만큼 다리를 넘어감
    for s in stones:
        # 해당 돌이 0 이하 => 표시
        if s - mid <= 0:
            ck += 1
        # 해당 돌이 아직 0이 아니면, 더 건널 수 있음
        else:
            ck = 0
        # 0 이하인 돌이 연속으로 k개 존재하면, 일단 가능한 친구 수는 아님!
        if ck >= k:
            return True
    
    return False


# 징검다리( 친구 = 무한, 돌 원소 값 max = 2억 ) + 선형 탐색 => 이진 탐색(효율성이 제일 좋음!)
def solution(stones, k):
    # 친구 수 범위 고려
    min_, max_ = 1, 200000000
    
    # 이진 탐색 수행 (MIN과 MAX의 차이가 1일때 까지(사이에 정수가 없을때 까지))
    while min_ < max_ -1 :
        # mid == 건넌 친구의 수
        mid = (min_ + max_) // 2
        
        # True => 연속으로 k개의 돌이 0인 경우,
        # 친구들 수가 해당 mid 보다 작은 경우에도 연속으로 k개가 나올 수 있음!
        if check(mid, stones, k):
            max_ = mid
        # False => 연속 k 개 돌이 0이 없는 경우,
        # 친구들 수가 해당 mid 보다 큰 경우에도 연속 k 개 돌이 0이 없을 수 있음!
        else:
            min_ = mid
    # 그 중 max 반환
    return max_