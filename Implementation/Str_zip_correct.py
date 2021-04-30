# 완전 탐색 문제
def solution(s):
    answer = len(s)

    # 1 ~ n/2 단위의 덩어리로 압축 ( ex) xyxy -> 2xy, n/2 이상부터는 오히려 커짐)
    for step in range(1,len(s) // 2 +1):
        # 압축될 문자열 & 시작 초기화
        compressed = ""
        prev = s[0:step]
        count = 1

        # 매번 덩어리 만큼 이동하면서
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이라면 => 압축 불가능
            else:
                # 해당 문법 기억하기 => prev가 2보다 크면 count 반영, 아니면 그냥 push
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 해당 덩어리로 prev 갱신 // count 초기화
                count = 1
        # 나머지 문자열 처리
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer