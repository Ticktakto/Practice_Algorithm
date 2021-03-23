import heapq

k = int(input())
food_times = list(map(int,input().split()))

def solution(food_times, k):
    # 전체 음식 먹는 time <= k -> -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 Greedy하게 뺀다. -> 우선순위 큐
    q = []
    for i in range(len(food_times)):
        # (food_time, food_num) queue insert    
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_val = 0 # 먹기 위해 사용한 시간
    prev = 0 # 직전에 다 먹은 음식 시간
    
    length = len(food_times) # 남은 음식 개수

    # sum_val + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수 와 k 비교
    # 먹는데 걸리는 시간이 작은 순의 음식 번호 순서대로 다 먹는데 걸리는 시간 계산
    # 해당 음식 번호가 다 먹으면 제외하면서, 직전 시간과 먹기 위해 쓴 시간 갱신
    while sum_val + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_val += (now - prev) * length
        length -= 1 # 다 먹은 음식 제외
        prev = now  # 이전 음식 시간 갱신

    # 남은 음식 중, 몇 번쨰 음식을 먹어야 할 지 계산
    res = sorted(q, key =lambda x:x[1]) # 음식 번호 순으로 정렬, 
    return res([k - sum_val] % length)[1]

print(solution(food_times, k))