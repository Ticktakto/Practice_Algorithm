# 보석 쇼핑 (https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3)

# list 중복 제거 => set()
# map 자료구조 -> dict 자료구조 
# 구간 문제 -> 시작점 & 끝점 & 중복 제거 위한 set + dict(빈도수 측정) 

def solution(gems):
    size = len(set(gems))
    # gems[0] 삽입 & answer 초기화
    dic = {gems[0]:1}
    temp = [0,len(gems) - 1]
    start, end = 0, 0

    # start & end 구간이 gems 범위 안에 있을 때 까지
    while start < len(gems) and end < len(gems):
        
        # 다 순회한 경우(gems 원소 검사 다 완료 시)
        if len(dic) == size:
            # 구간이 더 작은 값으로 갱신되면 temp 갱신
            if end - start < temp[1] - temp[0]:
                temp = [start, end]
            
            # start 증가하여, 새로운 구간으로 갱신
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        
        else:
            end += 1

            # 범위 벗어나면 종료
            if end == len(gems):
                break
            # 해당 값이 dict에 있다면
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            # 처음이면, dic에 넣으면서 초기화
            else:
                dic[gems[end]] = 1
    # temp => idx, idx 그러므로 1 더하기            
    return [temp[0] +1, temp[1] + 1]