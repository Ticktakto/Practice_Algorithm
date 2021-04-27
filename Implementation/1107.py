# https://pacific-ocean.tistory.com/424
import sys

input = sys.stdin.readline

# 해당 채널이, 고장난 버튼이 속한 digit이 존재하는 지
def check(num):
    num = list(str(num))
    for i in num:
        if i in s: return False
    return True

n = int(input())
m = int(input())
s = list(input().strip())

# 채널 100번에서 +,- 버튼만 누르는 횟수 경우 => 예외 케이스
result = abs(n - 100)

# 0번 채널 ~ 최악의 경우(모든 숫자의 경우의 수를 거치는 => 1,000,000번 채널)
# 1~2 초 => 백만 개의 데이터 리스트 처리 요구 시간의 border 값  
for i in range(1000001):
    # check => i 각 자릿수에 대해 고장난 버튼이 있는지 검사
    # 해당 숫자의 digit 개수 + 해당 숫자에서 n까지 +,-를 누르는 횟수
    if check(i): result = min(result, len(str(i)) + abs(i - n))
print(result)

# 중요한 것 => 최악의 경우를 생각하기, 예외 케이스 조건따라 곰곰히 생각해보기
