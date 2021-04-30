t = int(input())
num_arr = list(map(int,input().split()))
count = 0

for num in num_arr:
    temp = 0
    for is_num in range(1,num+1):
        if num % is_num == 0:
            temp += 1
    if temp == 2:
        count += 1

print(count)