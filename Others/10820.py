import sys

i = 0
while True:
    s = sys.stdin.readline().rstrip('\n')
    small, big, num, sp = 0, 0, 0, 0
    
    if not s:
        break

    for alpha in s:
        temp = ord(alpha)    
        if temp >= 97 and temp < 123:
            small += 1         
        if temp >= 65 and temp < 91:
            big += 1
        if temp >= 48 and temp < 58:
            num += 1
        if temp == 32:
            sp += 1
    sys.stdout.write("{} {} {} {}\n".format(small, big, num, sp))

