from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))

list_case = list(permutations(arr,n))
# 최악 => a, a, a, ...
res = 0

def Sum_Abs(arr):
    total_sum = 0
    for i in range(1,n):
        total_sum += abs(arr[i-1] - arr[i])
    
    return total_sum


for case in list_case:
    res = max(res, Sum_Abs(case))
print(res)
