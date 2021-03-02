# 배열 크기 N, 숫자가 더해지는 횟수 M, 연속해서 더할 수 있는 횟수 K
# 1 이상 10000 이하 자연수로 구성된 배열을 입력으로 받음

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# Greedy => 가장 큰 수를 k번 더하고, 두 번째로 큰 수를 1번 더한 후, 다시 가장 큰 수를 k번 반복
first_num = data[ n-1 ]
second_num = data[ n-2 ]


count = int( m / (k+1)) * k
count += m % (k+1)

res = 0
res += first_num * count
res += second_num * (m - count)

# 시간 초과를 해결하는 방법
print(res)