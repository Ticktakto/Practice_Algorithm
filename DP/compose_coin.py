# input
n, m = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

# DP ( bottom - up )

d = [10001] * 10001
d[0] = 0

for coin in range(n):
    for j in range(coins[coin], m + 1):
        if d[j - coins[coin]] != 10001: # 이미 해당 위치가 갱신이 된 경우
            d[j] = min(d[j], d[j-coins[coin]] + 1 )

if d[m] == 10001: # 목표가 주어진 동전으로 만들 수 없을 경우,
    print(-1)
else:
    print(d[m])