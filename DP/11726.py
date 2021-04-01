n = int(input())

dp = [0] * 1001
# 2*1 block 경우의 수
dp[1] = 1 
# 2*2 block 경우의 수
dp[2] = 2

for i in range(3,1001):
    dp[i] = dp[i-1] +  dp[i-2] + 1 - 1 # (1*n) * i는 중복이므로 뺸다
print(dp[n] % 10007) 