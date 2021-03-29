s = input()

len_of_zip = []


def Zip_Str(num):
    
    index = 0
    #res = 0
    zipper = []

    while num + index <= len(s):
        next_index = num + index
        zipper.append(s[index:next_index])
        index = next_index

    if s[index:len(s)]:
        zipper.append(s[index:len(s)])

    visited = [False] * len(zipper)
    res_str = []
    count = 1

    for i in range(len(zipper)):
        if visited[i] == False:
            
            visited[i] = True
            temp = zipper[i]
            
            for j in range(i+1,len(zipper)):
                if zipper[j] == temp:
                    count += 1
                    visited[j] = True
                else:
                    break
            
            if count == 1:
                res_str.append(temp)
            else:
                res_str.append(str(count) + temp)
            count = 1

        else:
            continue
    final_str = "".join(res_str) 

    return len(final_str)

for i in range(1,len(s)+1):
    myRes = Zip_Str(i)
    len_of_zip.append(myRes)

len_of_zip.sort()
print(len_of_zip[0])

'''
def solution(s):
    len_of_zip = []
    
    
    for i in range(1,len(s)+1):
        index = 0
        #res = 0
        zipper = []

        while i + index <= len(s):
            next_index = i + index
            zipper.append(s[index:next_index])
            index = next_index

        if s[index:len(s)]:
            zipper.append(s[index:len(s)])

        visited = [False] * len(zipper)
        res_str = []
        count = 1

        for i in range(len(zipper)):
            if visited[i] == False:
            
                visited[i] = True
                temp = zipper[i]
            
                for j in range(i+1,len(zipper)):
                    if zipper[j] == temp:
                        count += 1
                        visited[j] = True
                    else:
                        break
            
                if count == 1:
                    res_str.append(temp)
                else:
                    res_str.append(str(count) + temp)
                count = 1

            else:
                continue
        final_str = "".join(res_str) 
        len_of_zip.append(len(final_str))
    
    len_of_zip.sort()
    return len_of_zip[0]
'''