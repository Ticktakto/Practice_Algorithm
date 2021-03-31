from itertools import permutations

# 문제 조건 => 최대 친구가 8명 => 완전 탐색으로 처리 가능!
# 각 친구들을 모두 구별하여 나열하는 경우의 수 => 순열
# 해당 경우의 수 각각에 대해 취약 지점을 검사

def solution(n, weak, dist):
    # 문제가 원형으로 주어졌을 때 처리 방법! <= 반시계 방향 따로 생각 x
    # 원형 -> 일자 형태로 변환 (취약지점이 2번 반복)
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n) # n + 원래 취약지점 만큼 추가

    answer = len(dist) + 1 # 투입 친구 최솟값 찾기, 해당 값으로 초기화

    # 0 ~ n - 1 까지의 위치를 다 시작점으로 설정해서
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist,len(dist))):
            count = 1 # 투입할 친구 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count -1]
            # 시작점 부터 모든 취약 지점을 확인
            for index in range(start, start+length):
                # 점검할 수 있는 위치 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구 투입
                    if count > len(dist): # 더 투입이 불가능하면
                        break  # 종료
                    # 위치 갱신
                    position = weak[index] + friends[count-1]
        answer = min(answer,count) # get min val
    if answer > len(dist):
        return -1
    return answer