# 특정 원소가 속한 집합을 찾기 (경로 압축)
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    # a,b의 루트 노드를 얻어서
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 루트 노드 크기 조건 따라 병합
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 개수 & 간선(union 연산)개수 입력
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합을 출력
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent,i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블 : ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')