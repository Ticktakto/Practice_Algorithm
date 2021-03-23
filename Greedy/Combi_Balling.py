n, m = map(int, input().split())

arr = list(map(int, input().split()))

# weight => 1 ~ 10
weight_ball = [0] * 11

for x in arr:
    weight_ball[x] += 1

res = 0
# 1 ~ m 까지 각 무게에 대해 Greedy 처리
for i in range(1, m+1):
    n -= weight_ball[i] # 무게가 i인 볼링공 개수(A가 선택할 수 있는 개수) 제외
    res += weight_ball[i] * n # B가 선택하는 경우의 수와 곱하기

print(res)
    
