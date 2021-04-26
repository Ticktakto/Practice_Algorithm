#https://suri78.tistory.com/151
# 너무 어려운 문제, 다시 꼼꼼하게 읽어보기
import sys

n, m = map(int, sys.stdin.readline().split())
# ex) 123
#     456
#     789 같은 입력 받을 때 유용한 형식
rect = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
res = 0

# ||| 형식으로 3개 
for i in range(1,m-1):
    for j in range(i+1,m):
        s1 = sum([rect[a][b] for a in range(n) for b in range(i)]) 
        s2 = sum([rect[a][b] for a in range(n) for b in range(i,j)])
        s3 = sum([rect[a][b] for a in range(n) for b in range(j,m)])
        res = max(res, s1*s2*s3)

# ||
# -- 형식으로 3개
for i in range(1, m):
    for j in range(1, n):
        s1 = sum([rect[a][b] for a in range(j) for b in range(i)])
        s2 = sum([rect[a][b] for a in range(j) for b in range(i, m)])
        s3 = sum([rect[a][b] for a in range(j, n) for b in range(m)])
        res = max(res, s1*s2*s3)

# --
# || 형식으로 3개
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([rect[a][b] for a in range(i) for b in range(m)])
        s2 = sum([rect[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([rect[a][b] for a in range(i, n) for b in range(j, m)])
        res = max(res, s1*s2*s3)

# =| 형식으로 3개
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([rect[a][b] for a in range(i) for b in range(j)])
        s2 = sum([rect[a][b] for a in range(i, n) for b in range(j)])
        s3 = sum([rect[a][b] for a in range(n) for b in range(j, m)])
        res = max(res, s1*s2*s3)

# |= 형식으로 3개
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([rect[a][b] for a in range(i) for b in range(j, m)])
        s2 = sum([rect[a][b] for a in range(i, n) for b in range(j, m)])
        s3 = sum([rect[a][b] for a in range(n) for b in range(j)])
        res = max(res, s1*s2*s3)
# |
# |
# | 형식으로 3개
for i in range(1, n-1):
    for j in range(i+1, n):
        s1 = sum([rect[a][b] for a in range(i) for b in range(m)])
        s2 = sum([rect[a][b] for a in range(i, j) for b in range(m)])
        s3 = sum([rect[a][b] for a in range(j, n) for b in range(m)])
        res = max(res, s1*s2*s3)

print(res)
