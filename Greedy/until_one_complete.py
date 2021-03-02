n, k = map(int, input().split())

res = 0

while True:
    # ( N == k 로 나누어 떨어지는 수)가 될 때 까지 1을 한꺼번에 빼기
    temp = (n // k) * k     # 25 // 3 = 8, 8 * 3 = 24
    res += n - temp     # 1을 뺀 횟수
    
    if n < k:
        break

    n //= k
    res += 1

res += (n - 1)      # 마지막 남은 나머지 ( n보다 작은 수 ) 대해 1씩 뺀 횟수 더하기

print(res)