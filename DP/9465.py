# https://pacific-ocean.tistory.com/197
# max & min + dp 유형
t = int(input())

for i in range(t):
    arr_map = []
    n = int(input())

    # get input
    for k in range(2):
        arr_map.append(list(map(int, input().split())))
    
    # n = 2 에 대해서 초깃값 얻기
    arr_map[0][1] += arr_map[1][0]
    arr_map[1][1] += arr_map[0][0]

    # 점화식 => j 번째 스티커에 대해서, 왼쪽 대각선 숫자나 그 숫자의 왼쪽 숫자에 대해 더한 값에서 큰 값 추출
    for j in range(2, n):
        arr_map[0][j] += max(arr_map[1][j - 1], arr_map[1][j - 2])
        arr_map[1][j] += max(arr_map[0][j - 1], arr_map[0][j - 2])

    # 규칙을 못 구했음, dp를 input 형태 그대로 사용하는 줄 몰랐음.
    print(max(arr_map[0][n - 1], arr_map[1][n - 1]))

    