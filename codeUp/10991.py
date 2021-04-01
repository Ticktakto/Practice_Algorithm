t = int(input())

blank = t

for i in range(1,t+1):
    blank -= 1

    temp = ''
    temp2 = ''
    temp3 = ''
    can_change = ''
    for k in range(blank):
        temp2 += ' '
    for j in range(i):
        if j % 2 == 0:
            temp += '*'
            can_change = '*'
        else:
            temp += ' '
            can_change = ' '
    for p in range(i-1):
        if can_change == ' ':
            temp3 += '*'
            can_change = '*'
        elif can_change == '*':
            temp3 += ' '
            can_change = ' '
    print(temp2 + temp + temp3) 
