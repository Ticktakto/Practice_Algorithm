t = int(input())

for _ in range(t):
    ps = input()
    arr = []
    is_ps = [False] * len(ps)
    
    index = 0
    for p in ps:
        arr.append(p)
        
        left = 0
        right = 0

        for k in arr:
            if k == '(':
                left += 1
            if k == ')':
                right += 1
        if left < right:
            break    
        if left == right and arr[-1] == ')':
            is_ps[index] = True
        index += 1

    if is_ps[-1] == True:
        print("YES")
    else:
        print("NO")
        
        