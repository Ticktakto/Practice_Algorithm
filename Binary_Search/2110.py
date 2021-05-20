# https://claude-u.tistory.com/448
# 아이디어 접근(gap을 이진탐색하면서, c개로 배분되도록 할당된 집 개수를 세기)은 맞았지만, 확실치 않아 고민해서 틀림..
n, c = map(int, input().split())
house_ = []

for _ in range(n):
    house_.append( int(input()) )

house_.sort()
start, end = 1, house_[-1] - house_[0]

# 해당 간격의 범위에 집(원소)이 있는지 검사, get count (이걸 구현하지 못했음!)
def get_house(gap):
    count, house_pointer = 1, house_[0]

    for i in range(1,n):
        if house_pointer + gap <= house_[i]:
            count += 1
            house_pointer = house_[i]
    
    return count

res = 0

# 반복문 이진 탐색
while start <= end:
    mid = (start + end) // 2

    # c보다 많을수록(같거나), gap을 증가! => 인접된 공유기 간 거리가 max하는 방향으로 순회하게 된다.
    if get_house(mid) >= c:
        res = mid
        start = mid + 1
    # 아니면 gap을 감소
    else:
        end = mid - 1

print(res)



