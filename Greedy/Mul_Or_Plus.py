s = input()

arr = []
for num in s:
    arr.append(int(num))

arr.sort()

res = arr[0]

for i in range(1, len(arr)):
    if res == 0 or res == 1:
        res += arr[i]
        continue

    if arr[i] == 0 or arr[i] == 1:
        res += arr[i]
    else:
        res *= arr[i]

print(res)