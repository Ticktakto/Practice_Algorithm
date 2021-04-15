# https://pacific-ocean.tistory.com/208
n = int(input())

dp = [0 for i in range(31)]
dp[2] = 3

for i in range(3,31):
    # 홀수인 경우, 만들 경우가 없음
    if i % 2 != 0:
        continue
    else:
        # 이전의 경우에 3번 곱한 경우가 생김
        dp[i] = dp[i-2] * 3
        for j in range(4,i,2):
            # 이전의 새로운 경우(중앙 1*2)들 * 나머지 부분 조합
            dp[i] += dp[i-j] * 2
        # 아예 새로운 경우 (중앙에 1*2 블럭이 이어지는 경우)
        dp[i] += 2

print(dp[n])
