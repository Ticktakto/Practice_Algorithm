t = int(input())
block = t

for j in range(1,t+1):
    block -= 1
    temp = ''
    temp2 = ''
    for i in range(j):
        temp += '*'
    for k in range(block):
        temp2 += ' '
    
    print(temp2 + temp)