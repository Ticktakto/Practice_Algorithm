a, b, c = map(int, input().split())

res1 = (a+b)%c
res2 = ((a%c) + (b%c)) % c
res3 = (a*b)%c
res4 = ((a%c) * (b%c)) % c

print(res1)
print(res2)
print(res3)
print(res4)