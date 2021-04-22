S = input()

arr = [-1 for i in range(26)]
index = 0

for alpha in S:
    num = ord(alpha) - 97
    for i in range(26):
        if arr[i] != -1:
            continue
        if num == i:
            arr[i] = index
    index += 1

str_arr = [str(i) for i in arr]
print(' '.join(str_arr))