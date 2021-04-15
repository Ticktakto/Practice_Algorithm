n = int(input())

dp = [1 for i in range(101)]

dp[0] = 0
dp[4] , dp[5] = 2, 2
dp[6], dp[7] = 3, 4

for i in range(8,101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(n):
    data = int(input())
    print(dp[data])