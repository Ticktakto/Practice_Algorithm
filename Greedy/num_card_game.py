
n, m = map(int, input().split())

res = 0

for i in range(n):
        
        CardNum = list(map(int, input().split()))
        min_val = 10001

        for data in CardNum:
            min_val = min(min_val, data)
        
        res = max(res, min_val)

print(res)