n = input()
res = sorted(n)
res=''.join(res)

remove_list = []
for i in res:
    try:
        remove_list.append(int(i))
        index = res.index(i)
    except ValueError:
        res = res[index+1:]
        break

res += str(sum(remove_list))
print(res)

