N, K = map(int, input().split())


A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)


for i in range(K):
    if A[i] < B[i]: # A 제일 작은 원소가 B 제일 큰 원소보다 더 큰 경우엔 바꿔주면 안된다!
        A[i] , B[i] = B[i], A[i]

    else:
        break


print(sum(A))
