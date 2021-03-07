array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i, 0, -1): # i 부터 1까지 감소하며 반복
        
        if array[j] < array[j-1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break # 자기보다 작은 데이터 만나면 거기서 멈춤
print(array)