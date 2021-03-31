while True:
    # try - except!
    try:
        a, b = map(int, input().split())
        print(a+b)
    except: # 입력 케이스가 없을 경우
        break