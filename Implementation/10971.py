# https://copy-driven-dev.tistory.com/entry/백준Python10971브루트포스-외판원-순회-2

from itertools import permutations

n = int(input())
travel = [list(map(int, input().split())) for _ in range(n)]
travel_start  = [i for i in range(n)]
res = int(1e9)

# cites_route => 나열 순서가 이동하는 순서임!
def progress_add(cites_route):
    global travel, n
    tmp = 0

    for i in range(len(cites_route)-1):
        if travel[cites_route[i]][cites_route[i+1]] != 0:
            tmp += travel[cites_route[i]][cites_route[i+1]]
        
        else:
            return -1
    # 사이클 (이동 순서의 마지막 지점) -> 다시 시작점으로
    if travel[cites_route[-1]][cites_route[0]] == 0:
            return -1
    else:
        tmp += travel[cites_route[-1]][cites_route[0]]
    return tmp

# 시작점 -> 여러 경로 (n개 만큼 다 거친 경우)
for routes in permutations(travel_start):
    route_val = progress_add(routes)

    # 만약 경로를 더 진행할 수 없는 경우엔 제외하기(back-tracking)
    if route_val != -1:
        res = min(res, route_val)
print(res)
    


