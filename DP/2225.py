# https://pacific-ocean.tistory.com/210
n, k = map(int, input().split())

dp = [[0] * 201 for i in range(201)]

for i in range(1,201):
    dp[i][1] = 1

for i in range(1,201):
    for j in range(201):
        for k in range(j+1):
            dp[j][i] += dp[k][i-1]

print(dp[n][k] % 1000000000)