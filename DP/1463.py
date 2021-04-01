# Greedy or Dynamic Programming
# 1st, DP
n = int(input())

d = [0] * (1000001)
d[0] = 0
d[1] = 0
d[2], d[3] = 1, 1

for i in range(1,n+1):
    if i == 1 or i == 2 or i == 3:
        continue
    is_div_3 = 100000
    is_div_2 = 100000
    if i%3 == 0:
        is_div_3 = d[i//3] + 1
    if i%2 == 0:
        is_div_2 = d[i//2] + 1
    non_div = d[i-1] + 1

    d[i] = min(non_div, is_div_2, is_div_3)
print(d[n])