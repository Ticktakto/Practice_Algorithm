t = int(input())
block = 0

for j in range(t,0,-1):
    temp = ''
    temp2 = ''
    for i in range(j):
        temp += '*'
    for j in range(block):
        temp2 += ' '
    block += 1
    print(temp2 + temp)