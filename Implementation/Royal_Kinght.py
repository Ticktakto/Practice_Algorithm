
# 입력받기
input_data = input()
col_types = ['a','b','c','d','e','f','g','h']
col = input_data[0]
row = int(input_data[1])

# 이동 정의

point = [col_types.index(col), row - 1]
print(point)
move_types = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [-1,2], [1,-2], [-1,-2]]


# 체스판에서 움직임 정의

res = 0

for idx in move_types:
    count = [point[0] + idx[0], point[1] + idx[1]]
    print(count)

    if count[0] < 0 or count[0] >= 8 or count[1] < 0 or count[1] >= 8:
        continue
    
    res += 1


# 결과 출력
print(res)