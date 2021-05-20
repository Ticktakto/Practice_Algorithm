# https://claude-u.tistory.com/448
# 아이디어 접근(gap을 이진탐색하면서, c개로 배분되도록 할당된 집 개수를 세기)은 맞았지만, 확실치 않아 고민해서 틀림..
n, c = map(int, input().split())
house_ = []

for _ in range(n):
    house_.append( int(input()) )

house_.sort()
start, end = 1, house_[-1] - house_[0]

res = 0
# 반복문 이진 탐색
while start <= end:
    mid = (start + end) // 2
    prev_, count = house_[0], 1
    # 집 간 거리가 간격보다 큰지 작은지 조사 -> 집 간 거리가 간격보다 더 크면 해당 간격에 상관없이 배정한다. 
    for tmp in house_[1:]:
        if (tmp - prev_) >= mid:
            count += 1
            prev_ = tmp
    
    # c보다 많을수록(같거나), gap을 증가! => 인접된 공유기 간 거리가 max하는 방향으로 순회하게 된다.
    if count >= c:
        res = max(res, mid)
        start = mid + 1
    # 아니면 gap을 감소
    else:
        end = mid - 1

print(res)



