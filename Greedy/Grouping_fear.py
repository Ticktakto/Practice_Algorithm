n = int(input())

arr = list(map(int, input().split()))

arr.sort()

res = 0
group = 0

for i in arr:
    group += 1
    if group >= i:
        res += 1
        group = 0

print(res)
