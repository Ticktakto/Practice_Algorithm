N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

res = sorted(arr, reverse=True)

print(res)