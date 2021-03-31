data = input()
count = 0
temp = ""

for i in range(len(data)):
    temp += data[i]
    count += 1
    if count == 10:
        print(temp)
        temp = ""
        count = 0
    if i == len(data) - 1:
        print(temp)
        
