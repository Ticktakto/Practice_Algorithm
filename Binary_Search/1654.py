# 8:05 ~ 9:00

k, n = map(int, input().split())
lanson_ = []

for _ in range(k):
    lanson_.append(int(input()))

start, end = 1, max(lanson_)
res = 0

# 이진탐색 (반복문) => start == end 될 때 까지
while start <= end:
    # mid = 해당 길이로 나눌 기준
    mid = (start + end) // 2

    is_n = 0
    for lan_ in lanson_:
        # 기준 만큼 쪼개서 나온 랜선 개수만큼 추가
        is_n += (lan_ // mid)
    
    # n개보다 같거나 많으면 => Ok, 그 때 랜선 길이 비교
    if is_n >= n:
        start = mid + 1
        res = max(res, mid)
    # 적으면, 기준 길이를 더 작게 잡는다.
    else:
        end = mid - 1

print(res)
    