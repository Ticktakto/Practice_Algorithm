array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2] # 모든 원소는 0보타 크거나 같은 양의 정수

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1    # 각 데이터에 해당되는 인덱스의 값 증가 ( 실제 배열과 인덱스(양의 정수)와 매칭 )

for i in range(len(count)): # 리스트에 기록된 정렬 정보 출력
    for j in range(count[i]):
        print(i, end=' ')   # 등장 횟수만큼 인덱스 출력
