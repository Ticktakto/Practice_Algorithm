t = int(input())

for _ in range(t):
    
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(arr[index:index+m])
        index += m

    for i in range(1,m):        
        for j in range(n):

            if j == 0:
                left_up = 0
            else:
                left_up = dp[j-1][i-1]           
            if j == n-1:
                left_down = 0
            else:
                left_down = dp[j+1][i-1]
            left = dp[j][i-1]
            dp[j][i] = dp[j][i] + max(left, left_down, left_up)

    res_num = 0
    for i in range(n):
        res_num = max(res_num, dp[i][m-1])
    print(res_num)
        



