n = int(input())

# 앞선 결과를 저장하기 위한 Table ( n은 1 이상 30000 이하 )
d = [0] * 30001

# DP 진행 ( bottom - up )
for i in range(2, n+1):
    # n - 1
    d[i] = d[i-1] + 1

    # d[i]가 1 더한 값으로 갱신되고, 이 때 i가 해당 숫자로 나눠질 수 있으면, 갱신

    # n % 2 == 0
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1) 
    # n % 3 == 0
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1) 
    # n % 5 == 0
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1) 

print(d[n])

