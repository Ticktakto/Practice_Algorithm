# 호텔 방 배정 (https://programmers.co.kr/learn/courses/30/lessons/64063)

def check(real_room, guest, k):
    for i in range(guest+1, k-1):
        if real_room[i] == 1:
            return i

    
def solution(k, room_number):
    answer = []
    real_room = [1 for i in range(k)]
    
    for guest in room_number:
        if real_room[guest] == 1:
            answer.append(guest)
            real_room[guest] -= 1
        
        else:
            fixed_ = check(real_room, guest, k)
            answer.append(fixed_)
            real_room[fixed_] -= 1
    
    return answer