t = int(input())
res = []

for _ in range(t):
    a, b = map(int, input().split())
    res.append(a+b)

for i in res:
    print(i)