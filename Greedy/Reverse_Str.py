s = input()

zero_num = 0
one_num = 0

for i in s:
    if int(i) == 0:
        zero_num += 1
    else:
        one_num += 1

def count_num(num):
    
    first = s.index(str(num))
    temp = 0
    count = 0
    
    for i in range(int(first), len(s)):
        if int(s[i]) == num:
            temp += 1
            if temp == 1:
                count += 1

        else:
            temp = 0

    print(count)

if zero_num > one_num :
    count_num(1)
else:
    count_num(0)     