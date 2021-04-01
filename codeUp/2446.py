t = int(input())
block = t
blank = 0
length = 2 * t - 1

for i in range(1,length+1):
    temp = ''
    temp2 = ''
    temp3 = ''
    
    if i <= t:
        for j in range(block):
            temp += '*'
        for k in range(blank):
            temp2 += ' '
        block -= 1
        blank += 1
        for p in range(block):
            temp3 += '*'
        if i == t:
            block = 1
            blank = t-1
    else:
        block += 1
        blank -= 1
        for z in range(block):
            temp += '*'
        for y in range(blank):
            temp2 += ' '
        for x in range(block-1):
            temp3 += '*'

    print(temp2 + temp + temp3)

