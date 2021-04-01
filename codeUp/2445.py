t = int(input())

count = 2 * t - 1
block = t
blank = t

for i in range(1,count+1):
    temp = ''
    temp2 = ''
    temp3 = ''
    if i <= t:
        blank -= 1
        for j in range(i):
            temp += '*'
        for k in range(blank):
            temp2 += ' '
        temp3 = temp2 + temp
    else:
        block -= 1
        blank += 1
        for j in range(block):
            temp += '*'
        for j in range(blank):
            temp2 += ' '
        temp3 = temp2 + temp
    print(temp + temp2 + temp3)