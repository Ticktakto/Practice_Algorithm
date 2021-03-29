#input
from itertools import combinations

# n => n * n matrix, m => 최대 고를수 있는 m 개 치킨집
n, m = map(int, input().split())

chicken, house = [], []

# input matrix
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            # house 좌표 get
            house.append((r,c))
        elif data[c] == 2:
            # chicken 좌표 get
            chicken.append(r,c)

# 모든 치킨집 중, m개의 치킨집을 뽑는 경우 => 조합!
candidates = list(combinations(chicken, m))

# 치킨 거리의 합 계산
def get_sum(candidates):
    res = 0
    for hx, hy in house:
        # min 초기화
        temp = 1e9
        for dx, dy in candidates:
            # 거리 계산 (절댓값) -> 작은 값 구하기
            temp = min(temp, abs(hx - dx) + abs(hy - dy))
        # res += 각 집의 치킨 거리 (특정 치킨집과 가장 가까운 거리)    
        res += temp
    return res

# 치킨 거리 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    # candiate => 조합의 원소 => 해당 치킨집들의 각각 조합의 경우
    result = min(result, get_sum(candidate))
