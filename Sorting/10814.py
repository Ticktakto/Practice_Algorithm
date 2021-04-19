# https://claude-u.tistory.com/149
n = int(input())

arr = []
for _ in range(n):
    age, name = input().split()
    arr.append([int(age),name])

for i in sorted(arr,key=lambda member: (member[0])):
    print( i[0], i[1] )