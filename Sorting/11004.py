n, k = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort(reverse=False)
print(arr[k-1])