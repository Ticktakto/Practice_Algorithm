num, change = map(int,input().split())

num_range = [str(i) for i in range(36)]

for i in range(10,36):
    num_range[i] = chr(i + 55)

res = ''

while num != 0:
    temp = num % change
    num //= change
    res += num_range[temp]

print(res[::-1])