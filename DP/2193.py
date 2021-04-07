n = int(input())

dp = []
dp.append(0)
dp.append(1)
dp.append(1)

for i in range(3,91):
    temp = dp[i-1] + dp[i-2]
    dp.append(temp)

print(dp[n])