s = input()

small_arr = [i+97 for i in range(26)]
big_arr = [i+65 for i in range(26)]

restart_small = 0
restart_big = 0

for i in range(26):
    rot_13_small = small_arr[i] + 13
    rot_13_big = big_arr[i] + 13

    if rot_13_small >= 123:
        rot_13_small = 97 + restart_small
        restart_small += 1
    if rot_13_big >= 91:
        rot_13_big = 65 + restart_big
        restart_big += 1
    
    small_arr[i] = rot_13_small
    big_arr[i] = rot_13_big

res = ''
for alpha in s:
    tmp = ord(alpha)
    
    if tmp >= 97 and tmp <= 122:
        res_tmp = small_arr[tmp - 97]
        res += chr(res_tmp)
        continue

    elif tmp >= 65 and tmp <= 90:
        res_tmp = big_arr[tmp-65]
        res += chr(res_tmp)
        continue
    
    else:
        res += alpha
print(res)