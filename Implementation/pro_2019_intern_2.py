
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):

    s = s.replace("{","[")
    s = s.replace("}","]")
    s = eval(s)

    s.sort(key=lambda x: len(x))
    
    answer = [s[0][0]]
    #ans_idx = 0
    for t in s[1:]:

        for each_num in t:
            if each_num not in answer:
                answer.append(each_num)
        #ans_idx += 1
    print(answer)    
    return answer

solution(s)