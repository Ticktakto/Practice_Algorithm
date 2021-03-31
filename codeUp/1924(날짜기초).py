# 날짜 문제 풀 때 참고!
mon, day = map(int,input().split())

daysOfMon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
nameOfDays = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

# 총 일수 = 입력받은 mon 만큼, 해당 요일을 모두 더하기
for i in range(1,mon):
    day += daysOfMon[i]

# 1월 1일이 월요일이므로 총 일수를 7로 나눈 나머지가 요일
print(nameOfDays[day % 7])