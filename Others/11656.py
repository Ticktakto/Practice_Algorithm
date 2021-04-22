s = input()
arr = []

for i in range(len(s)):
    tmp = s[i:len(s)]
    arr.append(tmp)

arr.sort()
for i in range(len(arr)):
    print(arr[i])

