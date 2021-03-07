array1 = [5,7,9,0,3,1,6,2,4,8]
array2 = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr,start,end):
    # 재귀 종료 조건, 원소가 1인 경우
    if start >= end:
        return
    pivot = start    
    left = start + 1
    right = end

    while left <= right :
        # pivot보다 큰 데아터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot] :
            left += 1

        # pivot보다 작은 데이터를 찾을 때 까지 반복
        while right > start and arr[right] >= arr[pivot] :
            right -= 1
    
        # 엇갈렸다면 작은 데이터와 pivot을 교체
        if left >= right :
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교채
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # pivot 중심, 좌 우 리스트에 대해 재귀적으로 호출
    quick_sort(arr, start, right - 1 )
    quick_sort(arr, right + 1, end)

def python_quick_sort(arr): # 시간 복잡도에선 조금 비효율적이나, 기억하기 더 쉬운 방법!
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # pivot
    tail = arr[1:]  # 나머지

    left_side = [x for x in tail if x <= pivot] # 왼쪽 리스트
    right_side = [x for x in tail if x > pivot] # 오른쪽 리스트

    # 분할 이후, 왼쪽, 오른쪽 각각 재귀적으로 정렬 수행 후 전체 리스트 반환
    return python_quick_sort(left_side) + [pivot] + python_quick_sort(right_side)

print(python_quick_sort(array1))

quick_sort(array2,0,len(array2) - 1)
print(array2)    
    