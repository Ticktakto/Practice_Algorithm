# 2020 kakao - intern-ship
def search(num_board, num):
    for y in range(4):
        for x in range(3):
            if num_board[y][x] == num:
                return y, x

def solution(numbers, hand):
    left_num = [1,4,7]
    right_num = [3,6,9]
    middle_num = [0,2,5,8]
    
    num_board = [[0] * 3 for _ in range(4)]
    num_ = 1
    
    for i in range(4):
        for j in range(3):
            if i == 3 and j == 1:
                continue
            num_board[i][j] = num_
            num_ += 1
            
    left_finger_y, left_finger_x = 3, 0
    right_finger_y, right_finger_x = 3, 2
    answer = ''
    for num in numbers:
        finger_y, finger_x = search(num_board, num)
        if num in left_num:
            answer += 'L'
            left_finger_y, left_finger_x = finger_y, finger_x
        if num in right_num:
            answer += 'R'
            right_finger_y, right_finger_x = finger_y, finger_x
            
        if num in middle_num:
            
            leng_right =  abs(finger_y - right_finger_y) + abs(finger_x - right_finger_x)
            leng_left = abs(finger_y - left_finger_y) + abs(finger_x - left_finger_x)
            if leng_right > leng_left:
                left_finger_y, left_finger_x = finger_y, finger_x
                answer += 'L'
            elif leng_right < leng_left:
                right_finger_y, right_finger_x = finger_y, finger_x
                answer += 'R'
            elif leng_right == leng_left:
                if hand == 'left':
                    left_finger_y, left_finger_x = finger_y, finger_x
                    answer += 'L'
                else:
                    right_finger_y, right_finger_x = finger_y, finger_x
                    answer += 'R'
    return answer