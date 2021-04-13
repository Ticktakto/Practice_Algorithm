# https://pacific-ocean.tistory.com/206
n = int(input())
arr = list(map(int, input().split()))

dp = [0 for i in range(n)]
dp[0] = arr[0]

# 반례 -> arr = [2,1,5,6,7]
# arr 가 감소하는 범위에 대해서 고려하지 못했음. 
for i in range(1,n):
    temp = []
    for j in range(i):
        if arr[j] < arr[i]:
            temp.append(dp[j])
    if not temp:
        dp[i] = arr[i]
    else:
        dp[i] = arr[i] + max(temp)

print(max(dp))