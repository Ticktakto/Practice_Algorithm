n, k = map(int, input().split())

arr = [i for i in range(1,n+1)]
index = 0
leng = n
res = []

while True:
    if len(arr) == 0:
        break
    
    index += (k-1)
    index = index % leng
    
    tmp = arr[index]
    res.append(str(tmp))
    del arr[index]
    leng = len(arr)

print('<'+ ', '.join(res) +'>')
