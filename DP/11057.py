n = int(input())

dp = []
res_dp = []

dp.append([1 for i in range(10)]) # 1 -> index = 0

res_sum = 10
for i in range(1,1001):
    dp.append([1 for i in range(10)])
    dp[i][0] = res_sum
    
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
        res_sum += dp[i][j]


print(dp[n][0]% 10007)


