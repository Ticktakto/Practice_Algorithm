N = int(input())

arr = []

for i in range(N):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

def setting(data):
    return data[1]

res = sorted(arr, key=setting)

for data in res:
    print(data[0], end=' ')