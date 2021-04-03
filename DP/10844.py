# https://dev-wd.github.io/algorithm/backjoon10844/
# DP를 이렇게도 초기화 할 수 있음! (DP는 어떤 것을 저장하고, 꺼내 쓸까?)

n = int(input())

# DP의 의미 => 1의 맨 앞자리, 10의 맨 앞자리, 100의 맨 앞자리 ... 10^n의 맨 앞 자리
dp = []
dp.append([1 for i in range(10)]) # 0,1,2, ... , 9
for i in range(99): # n => 1 ~ 100 까지의 길이
    dp.append([0 for i in range(10)])

for i in range(99):
    for j in range(10):
        # ex) j == 2, 1과 3이 인접수, 경계인 0과 9는 한 번만 처리
        if j >= 1:
            dp[i+1][j-1] += dp[i][j]
        if j <= 8:
            dp[i+1][j+1] += dp[i][j]
# dp[n-1][0] => 0의 자릿수가 가장 앞인 경우는 없으므로 제외
print( ( sum(dp[n-1]) - dp[n-1][0] ) % 1000000000 )