# 경주로 건설 (https://programmers.co.kr/learn/courses/30/lessons/67259)
# https://hose0728.tistory.com/76
# BFS - > 주로 두 노드 (0,0) -> (n-1,n-1) 사이의 최단 경로를 찾고 싶을 때
# 탐색하면서 -> 직선이라면 100원, 코너라면 500원 추가
from collections import deque
board = [[0,0,0],[0,0,0],[0,0,0]]


def solution(board):
    n = len(board)

    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    answer = int(1e9)
    queue =  deque()
    # x좌표 & y좌표 방향 비용 순서로 push, (방향은 맨처음 시 -1로 설정)
    # 0 ~ 3 => direction index!
    queue.append((0,0,-1,0))
    # Set Dict {(x,y,direction) : cost }
    visited = {(0,0,0) : 0, (0,0,1): 0, (0,0,2): 0, (0,0,3): 0}

    # BFS (For min-cost == min route)
    while queue:
        x, y, dir1, cost = queue.popleft() 
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 안 에서 + 방문하지 않은 노드에 대해
            if -1 < nx < n and -1 < ny < n and not board[nx][ny]:
                newcost = cost
                # direction == -1, 방금 출발한 경우 => 방향이 없으므로 그냥 100 추가
                if dir1 == -1:
                    newcost += 100
                # 기존 방향과 진행 방향이 평행한 경우
                elif (dir1 - d) % 2 == 0:
                    newcost += 100
                # 기존 방향과 수직인 경우
                else:
                    newcost += 600

                # 목적지 도착 경우, 정답 값과 비교 => min한 값으로 갱신
                if nx == n - 1 and ny == n - 1 :
                    answer = min(answer, newcost)
                
                # 기존에 방문하지 않았거나, 방문했을 경우보다 비용이 적은 경우 => queue.append
                elif visited.get((nx,ny,d)) is None or visited.get((nx,ny,d)) > newcost:
                    visited[(nx,ny,d)] = newcost
                    queue.append((nx,ny,d,newcost))
    return answer

print(solution(board))