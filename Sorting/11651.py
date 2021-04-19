n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append([y,x])

for i in sorted(arr):
    # 뒤집은 좌표를 다시 원래대로 출력
    print(i[1], i[0])