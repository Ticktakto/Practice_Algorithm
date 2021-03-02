# 배열 크기 N, 숫자가 더해지는 횟수 M, 연속해서 더할 수 있는 횟수 K
# 1 이상 10000 이하 자연수로 구성된 배열을 입력으로 받음

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# Greedy => 가장 큰 수를 k번 더하고, 두 번째로 큰 수를 1번 더한 후, 다시 가장 큰 수를 k번 반복
first_num = data[ n-1 ]
second_num = data [ n-2 ]

res = 0

while True:
    for i in range(k):  # 가장 큰수를 k 번 더하기
        if m == 0:  # M 0이면 반복 탈출
            break
        res += first_num
        m -= 1  # M을 1 씩 감소

    if m == 0:  # M 0이면 반복 탈출
        break  

    res += second_num   # 두 번째로 큰 수는 1 번 더하기
    m -= 1

print(res) 
