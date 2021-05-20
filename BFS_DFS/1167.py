# https://developmentdiary.tistory.com/436?category=847525
# 해당 문제는 입력을 어떻게 처리해야 하는지 알아야 함! 
import sys

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n):
    # ex) 3 1 2 3 4 -1 => 3(시작 노드), [1(도착 노드), 2(간선의 값)], [3(도착 노드), 4(간선의 값)], -1(끝)
    String_ = list(map(int, input().split()))
    len_String = len(String_)
    
    for i in range(1, len_String//2):
        arr[String_[0]].append([ String_[2*i-1], String_[2*i] ])

res1 = [0 for _ in range(n+1)]

# 재귀 흐름 더 공부하기..
def dfs(arr, start, res):
    for node, val in arr[start]:
        if res[node] == 0:
            res[node] = res[start] + val
            dfs(arr, node, res)

# 아무 노드나 출발시켜 준다 (루트를 모르므로, 총 dfs는 2번 돌린다)
dfs(arr, 1, res1)
res1[1] = 0

max_, longest_node = 0, 0 # 최장 경로 노드를 구한다
for i in range(len(res1)):
    if max_ < res1[i]:
        max_ = res1[i]
        longest_node = i # 가장 큰 값 => 특정 노드에서 가장 멀리까지 갔음을 의미한다
# 값이 클수록, 제일 멀리 or 값이 큰 간선을 모두 거쳤다고 의미한다. => 특정 노드에 상관없이 최장 경로 노드가 구해진다. 

res2 = [0 for _ in range(n+1)] # 최장 경로 노드에서 다시 dfs 수행 => 해당 값이 트리의 지름
dfs(arr, longest_node, res2)
res2[longest_node] = 0
print(max(res2))