#https://seohyun0120.tistory.com/entry/백준-11054-가장-긴-바이토닉-부분-수열-풀이
n = int(input())

arr = list(map(int, input().split()))

# 해당 인덱스
increase = [1 for i in range(n)]
decrease = [1 for i in range(n)]

# 인덱스 0 부터 특정 인덱스 까지 => 증가함을 판별 (11053 유형) 
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            increase[i] = max(increase[i], increase[j]+1)

# 배열의 마지막부터 특정 인덱스 까지 => 증가함을 판별 (역순) 
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if arr[j] < arr[i]:
            decrease[i] = max(decrease[i], decrease[j]+1)

res = [0 for i in range(n)]
for i in range(n):
    res[i] = increase[i] + decrease[i] - 1

print(max(res))