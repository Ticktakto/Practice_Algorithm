t = int(input())
blank = t
block = 0
length = 2 * t - 1

for i in range(1,length+1):
    temp = ''
    temp2 = ''

    if i <= t:
        blank -= 1
        block += 1
        for j in range(i):
            temp += '*'
        for k in range(blank):
            temp2 += ' '
    else:
        blank += 1
        block -= 1 
        for p in range(blank):
            temp2 += ' '
        for q in range(block):
            temp += '*'
    print(temp2 + temp)
