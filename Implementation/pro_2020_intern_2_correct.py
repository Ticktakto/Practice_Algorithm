from itertools import permutations

def soluation(expression):

    # 숫자, 연산자로 분리
    sep_expression = []
    num = ''
    idx = 0
    answer = 0
    for digit in expression:
        if digit != '-' and digit != '*' and digit != '+': 
            num += digit
        else:
            sep_expression.append(num)
            sep_expression.append(digit)
            num = ''
        if idx == len(expression)-1:
            sep_expression.append(num)
        idx += 1
    
    # operator
    oper = ['+', '-', '*']
    for ordered_oper in permutations(oper):
        copy_expression = sep_expression
        for op in ordered_oper:
            idx = 0
            while idx < len(copy_expression):
                if copy_expression[idx] == op:
                    if op == '-':
                        cal = int(copy_expression[idx-1]) - int(copy_expression[idx+1])
                    elif op == '+':
                        cal = int(copy_expression[idx-1]) + int(copy_expression[idx+1])
                    else:
                        cal = int(copy_expression[idx-1]) * int(copy_expression[idx+1])

                    copy_expression = copy_expression[:idx-1] + list(str(cal).split()) + copy_expression[idx+2:]
                
                else:
                    idx += 1
        else:
            answer = max(answer, abs(int(copy_expression[0])))
    return answer
