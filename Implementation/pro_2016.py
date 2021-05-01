def solution(a, b):
    DAY_NAME = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    day = b
    #mon
    for i in range(1,a):
        day += days[i]
    
    return DAY_NAME[day % 7]