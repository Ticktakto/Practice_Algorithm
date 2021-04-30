n = int(input())
score = []
for _ in range(n):
    score.append(list(map(int, input().split())))

def soluation(stu_score):
    answer = ''
    leng = len(stu_score)
    score = [[0] * leng for _ in range(leng)]
    
    for x in range(leng):
        for y in range(leng):
            score[x][y] = stu_score[y][x]
    
    self_num = 0
    average = []
    for scores in score:
        tmp = len(score)
        min_, max_, self_score = min(scores), max(scores), scores[self_num]

        if tmp == 2:
            if min_ == max_:
                average.append(sum(scores) / 2)
            elif min_ == self_score:
                average.append(max_)
            elif max_ == self_score:
                average.append(min_)
        else:
            sum_ = sum(scores)

            if max_ == self_score:
                max_count = 0
                for i in scores:
                    if self_score == i:
                        max_count += 1
                # 유일한 최댓값
                if max_count == 1:
                    tmp -= 1
                    sum_ -= self_score

            elif min_ == self_score:
                min_count = 0
                for i in scores:
                    if self_score == i:
                        min_count += 1
                # 유일한 최솟값
                if min_count == 1:
                    tmp -= 1
                    sum_ -= self_score
            average.append(sum_ / tmp)

        self_num += 1

    for aver in average:
        if aver >= 90:
            answer += 'A'
        elif aver >= 80 and aver < 90:
            answer += 'B'
        elif aver >= 70 and aver < 80:
            answer += 'C'
        elif aver >= 50 and aver < 70:
            answer += 'D'
        elif aver < 50:
            answer += 'F'
    return answer
print(soluation(score))
