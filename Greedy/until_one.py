
n, k = map(int, input().split())

res = 0

while n >= k:   # 일반적인 경우, k로 나누어 질 수 있도록!
    if n % k != 0:
        n -= 1
        res += 1
    
    n = n / k
    res += 1

while n > 1:   # 계산된 n이 k보다 작을 경우, 예를 들어 n=3, k=4 이면 2번을 빼주어 1로 만듬
    n -= 1
    res += 1

print(res) 
