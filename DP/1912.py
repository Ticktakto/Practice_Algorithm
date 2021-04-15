#https://hjp845.tistory.com/121
n = int(input())
arr = list(map(int,input().split()))

dp = [x for x in arr]

# 계속 오른쪽에 있는 숫자를 더해가지만(양수인 경우 계속 더함 = 최대값 갱신)
# (음수) - (양수) 순서면, 음수에서 모든 합(음수일 때) < 양수 이므로, 양수가 위치한 인덱스의 dp는 양수 값 그대로
# => +,- 충분히 고려할 수 있다.
for i in range(1,n):
    dp[i] = max(dp[i], dp[i-1] + arr[i])

print(max(dp))