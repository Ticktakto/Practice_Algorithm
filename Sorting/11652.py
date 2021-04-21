# dict 예제!
import sys

n = int(input())
my_dict = {}

for i in range(n):
    num = int(sys.stdin.readline())
    
    # num이 dict에 없는 경우
    if num not in my_dict.keys():
        my_dict[num] = 1
    else:
        my_dict[num] = my_dict[num] + 1

# dict = {카드 값 : 카드 개수}    
# 카드 개수 기준으로 먼저 내림차순, 그리고 카드 값 기준으로 오름차순
sorted_dict = sorted(my_dict.items(), key=lambda x: (-x[1],x[0]))
print(sorted_dict[0][0])


