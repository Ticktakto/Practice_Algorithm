# https://infinitt.tistory.com/288
# 이분 탐색 => 단일 target일 경우 효율이 좋음! 여러 원소가 존재하고 중복이 있다면 dict 쓰는게 훨씬 효율적!!

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
find_ = list(map(int, input().split()))

dic = dict()

for i in cards:
    try:
        dic[i] += 1
    except:
        dic[i] = 1

for j in find_:
    try:
        print( dic[j],end=' ')
    except:
        print(0, end=' ')