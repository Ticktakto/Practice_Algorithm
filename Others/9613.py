from itertools import combinations

t = int(input())

def GCD(x,y):
    while(y):
        x, y = y, x % y
    return x

for _ in range(t):
    num_arr = list(map(int,input().split()))
    num_arr = num_arr[1:]
    res = 0

    # gcd -> 무조건 한번 계산 시 두 개의 수로만 계산됨!
    for a, b in combinations(num_arr, 2):
        res += GCD(a,b)
    print(res)
    