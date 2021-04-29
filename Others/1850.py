# https://claude-u.tistory.com/404

a, b = map(int, input().split())

# 해당 숫자의 규칙을 찾으면, 1의 숫자 개수 값들의 최대공약수 * '1'을 얻을 수 있음
def GCD(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y    

print('1' * GCD(a,b)) 