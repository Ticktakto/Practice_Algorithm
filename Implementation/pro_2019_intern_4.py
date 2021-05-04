# 호텔 방 배정 (https://programmers.co.kr/learn/courses/30/lessons/64063)
# 시간 효율성 풀이 => (https://m.blog.naver.com/js568/221957852279)
# 더 깔끔한 풀이 (https://programmers.co.kr/learn/courses/30/lessons/64063/solution_groups?language=python3)
# 재귀는 모두 iterative 하게 바꿀 수 있음을 유의!!
import sys
sys.setrecursionlimit(10000) # 재귀 허용깊이 임의로 지정

def find_empty_room(check, rooms): # 재귀 함수
    if check not in rooms.keys(): # 빈 방이면( 종료 조건 )
        rooms[check] = check + 1 # rooms에 새 노드 추가
        return check # 요청한 방

    empty = find_empty_room(rooms[check], rooms) # 재귀함수 호출
    rooms[check] = empty + 1 # (배정된 방+1)을 부모노드로 변경
    return empty # 새로 찾은 빈 방

    
def solution(k, room_number):
    rooms = dict() # {방번호: 바로 다음 빈방 번호}
    for num in room_number:
        check_in = find_empty_room(num,rooms)
    return list(rooms.keys())
# 잘 모르는거 =>
# 왜 dict? -> 시간 복잡도 효율성
# 재귀함수의 응용?