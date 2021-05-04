# 불량 사용자 (https://programmers.co.kr/learn/courses/30/lessons/64064)
from itertools import permutations

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]

def mapping(id_set,ban_id_set):
    for i in range(len(id_set)):
        # 길이가 다른 경우
        if len(id_set[i]) != len(ban_id_set[i]):
            return False

        # user의 각 아이디에 대해
        for j in range(len(id_set[i])):
            # *는 넘기고
            if ban_id_set[i][j] == '*':
                continue
            # 각 문자가 하나라도 다를 시
            if id_set[i][j] != ban_id_set[i][j]:
                return False
    return True    
    


def solution(user_id, banned_id):
    answer = []
    # user_id에서 banned_id 개수만큼 모든 경우의 수를 뽑아서
    for get_case in permutations(user_id,len(banned_id)):
        if mapping(get_case,banned_id): # 해당 경우에 대해 banned_id와 매핑
            get_case = set(get_case)# 중복 제거 (같은 경우는 모두 1가지로 취급)
            if get_case not in answer:
                answer.append(get_case)
    
    return len(answer)

