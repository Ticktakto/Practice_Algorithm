a, b = map(int, input().split())
m = int(input())

# 각 자리수의 값을 나타낸 것!!
a_num = list(input().split())

pow_num = len(a_num) - 1
ten_num = 0
res = []

# 해당 숫자 - > 10진수
for digit in a_num:
    temp = (pow(a,pow_num)) * int(digit)
    ten_num += temp
    pow_num -= 1
 
# 10진수 -> B 진법

res_num = []
    
while ten_num :
    temp = ten_num % b
    ten_num = ten_num // b
    # str 뒤집기?
    res_num.append(str(temp))
    
res_ = res_num[::-1]

print(" ".join(res_))
    
            
        

    
