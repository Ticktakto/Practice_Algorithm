# my sol => 나중에 리팩토링 해보기
def solution(answers):
    
    step_supo_one = [1,2,3,4,5]
    step_supo_two = [2,1,2,3,2,4,2,5]
    step_supo_three = [3,3,1,1,2,2,4,4,5,5]
    
    correct_one = 0
    correct_two = 0
    correct_three = 0
    
    index = 0
    for answer in answers:
        if answer == step_supo_one[index % 5]:
            correct_one += 1
        if answer == step_supo_two[index % 8]:
            correct_two += 1
        if answer == step_supo_three[index % 10]:
            correct_three += 1
        index += 1
    
    supo_answer = [correct_one, correct_two, correct_three]
    max_index = supo_answer.index(max(supo_answer))

    res = [max_index+1]
    for i in range(3):
        if i == max_index:
            continue
        else:
            if supo_answer[i] == supo_answer[max_index]:
                res.append(i+1)
    return res