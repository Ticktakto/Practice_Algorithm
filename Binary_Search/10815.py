n = int(input())
cards = list(map(int, input().split()))

m = int(input())
find_ = list(map(int, input().split()))

def binary_search(arr, num, n):
    start, end = 0, n-1
    
    while start <= end:
        mid =(start + end) // 2

        if arr[mid] == num:
            return 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

cards.sort()
for fid in find_:
    print(binary_search(cards,fid,n), end=' ')
        

