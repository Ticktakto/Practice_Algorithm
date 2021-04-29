num_range = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

num, change = input().split()
pow_num = len(num) - 1
res = 0

for digit in num:

    real_num = num_range.index(digit)
    temp = pow(int(change), pow_num)
    res += (temp * real_num)
    pow_num -= 1
    

print(res)