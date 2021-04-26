e, s, m = map(int,input().split())
   
E, S, M = 1, 1, 1
res = 1

while True:
    if E == e and S == s and M == m:
        break
    
    if E+1 > 15:
        E = 1
        
    elif E >= 1 and E < 15:
        E += 1
    
    if S+1 > 28:
        S = 1
        
    elif S >= 1 and S < 28:
        S += 1
    
    if M+1 > 19:
        M = 1
        
    elif M >= 1 and M < 19:
        M += 1
    res += 1

print(res)