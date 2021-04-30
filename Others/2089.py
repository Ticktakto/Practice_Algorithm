# https://suri78.tistory.com/119
n = int(input())

res = ''
# 0인 경우
if not n:
    print('0')
else:
    while n:
        if n%(-2):
            res = '1' + res
            n = n//-2 + 1
        else:
            res = '0' + res
            n //= -2
    print(res)