n = int(input())
student = []

for _ in range(n):
    name, kor, eng, math = input().split()
    student.append([name, int(kor), int(eng), int(math)])

student.sort(key=lambda student : (-student[1], student[2], -student[3], student[0]))
for i in student:
    print(i[0])

