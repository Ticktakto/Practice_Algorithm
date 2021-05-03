# 수식 최대화 (https://programmers.co.kr/learn/courses/30/lessons/67257)
from itertools import permutations

expression1 = "50*6-3*2"

def parsing(expression):
    
    num = ''
    res = []
    idx = 0
    for digit in expression:
        if digit != '-' and digit != '*' and digit != '+': 
            num += digit
        else:
            res.append(num)
            res.append(digit)
            num = ''
        if idx == len(expression)-1:
            res.append(num)
        idx += 1
    return res

def calc(oper, expression):
    expression_tmp = expression
    while len(expression_tmp) > 1:
        
        for op in oper:
            try:
                op_idx = 0
                for ele, idx in enumerate(expression_tmp):
                    if ele == op:
                        op_idx = idx
                
                    if op == '+':
                        res = int(expression_tmp[op_idx-1]) + int(expression_tmp[op_idx+1])
                        expression_tmp.insert(op_idx+2,str(res))
                        
                        for _ in range(3):
                            expression_tmp.remove(expression_tmp[op_idx - 1])
                        

                    elif op == '-':
                        res = int(expression_tmp[op_idx-1]) - int(expression_tmp[op_idx+1])
                        expression_tmp.insert(op_idx+2,str(res))
                        
                        for _ in range(3):
                            expression_tmp.remove(expression_tmp[op_idx - 1])
                                
                    elif op == '*':
                        res = int(expression_tmp[op_idx-1]) * int(expression_tmp[op_idx+1])
                        expression_tmp.insert(op_idx+2,str(res))
                    
                        for _ in range(3):
                            expression_tmp.remove(expression_tmp[op_idx - 1])
                print(expression_tmp)    
            except ValueError:
                continue    

    
    return expression_tmp[0]



def solution(expression):
    # 2. get per from ('+','-','*')
    operator = []
    for oper in expression:
        if oper not in operator:
            if oper == '*' or oper == '-' or oper == '+':
                operator.append(oper)
    oper_list = list(permutations(operator))
    

    answer = 0
    # calc following oper_list
    for opers in oper_list:
        for_exp = parsing(expression)
        print(opers)
        tmp = calc(opers, for_exp)
        print(tmp)
        answer = max(answer, abs(int(tmp)))

    return answer

print(solution(expression1))