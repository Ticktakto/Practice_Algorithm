#Stack
longStone = input()
longStone = longStone.replace("()","*")

stone_arr = []
res = 0

for Stone in longStone:
    if Stone == "(":
       stone_arr.append(0)
    if Stone == ")":
        tmp = stone_arr.pop()
        res += tmp+1
    if Stone == "*":
        stone_arr = [i+1 for i in stone_arr]

print(res)

        

