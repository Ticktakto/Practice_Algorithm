x, y = map(int, input().split())

# 최대 공약수 (유클리드 호제법)
def GCD(x,y):
    while(y):
        x, y = y, x % y
    return x
            
# 최소 공배수 (유클리드 호제법)
def LCM(x,y):
    res = (x*y) // GCD(x,y)
    return res

print(GCD(x,y))
print(LCM(x,y))


