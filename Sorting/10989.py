# https://hwiyong.tistory.com/253
# 8MB (메모리 부족)& (시간 초과)
import sys 

n = int(input()) 
check_list = [0] * 10001 

# 중복되는 것 체크!
for i in range(n): 
    # 더 빠르게 입력받기
    check_num = int(sys.stdin.readline())
    check_list[check_num] += 1

for i in range(10001): 
    if check_list[i] != 0: 
        for j in range(check_list[i]):
            print(i)
