# Find
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# Union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# input ( v, e )
v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False # Temp Cycle

for i in range(e):
    a, b = map(int, input().split())
    # 사이클 발생 시, 종료 (모든 노드를 검사하기 전, 두 노드 루트 노드가 같아진다면)
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print('cycle이 발생했습니다.')
else:
    print('사이클이 발생하지 않았습니다.')