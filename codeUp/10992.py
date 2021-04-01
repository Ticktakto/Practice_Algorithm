t = int(input())
blank = t

for i in range(1, t+1):
    blank -= 1
    temp = ''
    temp2 = ''
    temp3 = ''

    for j in range(blank):
        temp2 += ' '
    if i < t:
        for k in range(i):
            if k == 0:
                temp += '*'
            else:
                temp += ' '
        for q in range(i-1):
            if q == i-2:
                temp3 += '*'
            else:
                temp3 += ' '
    elif i == t:
        for k in range(i):
            temp += '*'
        for q in range(i-1):
            temp3 += '*'
    print(temp2 + temp + temp3)