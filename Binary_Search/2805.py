n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

res = 0

while (start <= end):
    
    mid = (start + end) // 2
    remainder_trees = 0

    for tree in trees:
        if tree > mid:
            remainder_trees += (tree - mid)

    if remainder_trees < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
        


        