n = int(input()) # 3 ~ 100, len(arr)
arr = list(map(int,input().split()))

d = [0] * 100

# DP ( bottom - up )

# Setting, 맨 왼쪽 창고와 그 인접 창고
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

# 일반적인 경우, 특정 위치 창고
for i in range(2,n):
    # arr[ i - 1 ]을 털기로 하면, 현재 위치(arr[i])는 털 수 없음
    # arr[i]을 털기로 하면, arr[i-2]도 털 수 있음
    d[i] = max( d[i - 1], d[i-2] + arr[i] )

# DP를 해결하기 위해선, 함수 진행과정 도식 + 점화식을 세우기!
print(d[n-1])