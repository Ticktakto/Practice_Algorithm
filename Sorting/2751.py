# 시간 초과 -> pypy3
# https://somjang.tistory.com/entry/BaeKJoon-2751번-수-정렬하기2-Python
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
res = []

# python에서 중복 제거하는 방법!
for i in arr:
    if i not in res:
       res.append(i)

print(arr)

'''
-> 속도 빠른 방법!
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

for i in arr:
    sys.stdout.write(str(i) + "\n")
'''