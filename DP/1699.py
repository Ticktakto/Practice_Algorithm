# https://pacific-ocean.tistory.com/205
n = int(input())
dp = [0 for i in range(n + 1)]

# 316 * 316 = 99,856
square = [i * i for i in range(1, 317)]


for i in range(1, n + 1):
    # ex) i = 11
    temp = []
    for j in square:
        # ex) 1,4,9
        if j > i:
            break
        # 11 - 1, 11 - 4, 11 - 9 (remainder)
        # dp[10] = 2, dp[7] = 4, dp[2] = 2
        temp.append(dp[i - j])
    # dp[10] + 1 => 3^2 + 1^2 + 1^2
    dp[i] = min(temp) + 1
print(dp[n])