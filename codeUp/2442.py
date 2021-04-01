t = int(input())
block = t
remain = 0

for j in range(1,t+1):
    block -= 1
    
    temp = ''
    temp2 = ''
    temp3 = ''
    
    for i in range(j):
        temp += '*'
    for k in range(block):
        temp2 += ' '
    for k in range(remain):
        temp3 += '*'
    
    remain += 1
    
    print(temp2 + temp + temp3)