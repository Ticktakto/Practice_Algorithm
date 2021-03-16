# find_parent
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union_parent
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# v, e, parents
v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선 담을 리스트, 최종 비용을 담을 변수
edges = []
res = 0

# parent 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 1째 원소, 비용 순으로 정렬
edges.sort()

# 간선을 하나 씩
for edge in edges:
    cost, a, b = edge
    # no Cycle 경우, 집합에 추가 (최소 신장 트리를 위한, 트리 구성)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b) # 병합
        res += cost # 비용을 계속 더하기

print(res) # 최소 신장 트리로 만들어진, 총 최소 비용