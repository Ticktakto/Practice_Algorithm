n, m = map(int, input().split())

rice_cake = list(map(int, input().split()))

# 반복문을 통한 이진 탐색 구현

start = 0
end = max(rice_cake) #  가장 긴 떡의 길이
res = 0

while (start <= end) :
    mid = (start + end) // 2

    reminder_rice = 0

    for rice in rice_cake:

        if rice > mid : # 잘랐을 때 남은 떡 계산
            reminder_rice += rice - mid

    # 남은 떡이 부족한 경우 더 많이 자르기 ( left search )
    if reminder_rice < m:
        end = mid - 1
    # 남은 떡이 충분한 경우 덜 자르기 ( right search )
    else :
        res = mid   # 최대한 덜 잘렸을 때가 정답 ( 떡이 m보다 많거나 같을 경우, res=mid 이면 이상적인 정답 )
        start = mid + 1

print(res)