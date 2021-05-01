# 4보다 큰 모든 짝수는 두 홀수 소수 합으로 표기 가능
import sys

# 에라토스테네스의 체
max_ = 1000000
check_ = [True for i in range(max_)]
for i in range(2, int(max_ ** 0.6)):
    if check_[i] == True:
        for j in range(i * 2, max_, i):
            if check_[j] == True:
                check_[j] = False

# 소수 = Ture
while True:
    n = int(input())

    if not n:
        break
    # i가 작을수록 -> b - a == n-i - i 가 크다
    for i in range(3,max_):
        if check_[i] == True:
            if check_[n-i] == True:
                print("%d = %d + %d"%(n , i , n-i))
                break        
    
