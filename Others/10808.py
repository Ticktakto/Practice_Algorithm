S = input()

arr = [0 for i in range(26)]

for alpha in S:
    num = ord(alpha) - 97
    for i in range(26):
        if num == i:
            arr[i] += 1
str_arr = [str(i) for i in arr]
print(' '.join(str_arr))
