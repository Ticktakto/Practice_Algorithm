# 입력
N = int(input())
market = list(map(int,input().split()))

M = int(input())
needs = list(map(int, input().split()))

market.sort()

# 이진 트리 탐색 구현
def binary_search(arr, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)

# needs 각 원소에 대해 이진 탐색을 수행하여 yes or no 출력

for idx in needs:
    res = binary_search(market, idx, 0, len(market) - 1)
    
    if res == True:
        print("yes", end=' ')
    else:
        print("no", end=' ')

