n = int(input()) # 1 ~ 1000
arr = [0]
arr += list(map(int, input().split())) # 각 원소당 1 ~ 10,000

dp = [0 for i in range(n+1)]
dp[1] = arr[1]

for i in range(2,n+1):
    temp = [arr[i]]
    for j in range(1,i):
        temp.append(dp[j] + arr[i-j])
    dp[i] = max(temp)

print(dp[n])