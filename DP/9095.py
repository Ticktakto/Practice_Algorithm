t = int(input())

input_num = []
for _ in range(t):
    input_num.append(int(input()))

dp = [0] * 12
dp[1] = 1
dp[2] = 2 # 1+1,2, => 2도 포함 
dp[3] = 4 #

for i in range(4,12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for j in input_num:
    print(dp[j])