n = input()

div_len = len(n) // 2
arr = []
for i in range(len(n)):
    arr.append(int(n[i]))

first = sum(arr[0:div_len])
second = sum(arr[div_len:len(arr)+1])

if first == second:
    print("LUCKY")
else:
    print("READY")
