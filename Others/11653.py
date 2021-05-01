n = int(input())

if n > 1:
    tmp = 2

    while n:
        
        if n % tmp == 0:
            
            if n // tmp == 1:
                print(tmp)
                break
            print(tmp)
            n = n // tmp
            tmp = 2

        else:
            tmp += 1
        