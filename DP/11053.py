# https://bitwise.tistory.com/215
n = int(input())

arr = list(map(int,input().split()))


dp = [1 for i in range(n)]

# 시작점이 이전 dp 값에서부터 시작하는 게 아니라, 처음 인덱스(0) ~ i 까지 범위를 매번 검사!
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))
        