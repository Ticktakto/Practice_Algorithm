# 경주로 건설 (https://programmers.co.kr/learn/courses/30/lessons/67259)

# BFS - > 주로 두 노드 (0,0) -> (n-1,n-1) 사이의 최단 경로를 찾고 싶을 때
# 탐색하면서 -> 직선이라면 100원, 코너라면 500원 추가
from collections import deque

board = [[0,0,0],[0,0,0],[0,0,0]]

def dfs(x,y,board,n,price):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if board[x][y] == 0:
        board[x][y] = 2

        # 직선
        if board[x-1][y] == 2:
            # 코너
            if board[x-1][y-1] == 2 or board[x-1][y+1] == 2:
                price += 500
            else:
                price += 100

        elif board[x][y-1] == 2:
            if board[x-1][y-1] == 2 or board[x+1][y-1] == 2:
                price += 500
            else:
                price += 100
        
        elif board[x+1][y] == 2:
            if board[x+1][y-1] == 2 or board[x+1][y+1] == 2:
                price += 500
            else:
                price += 100
        
        elif board[x][y+1] == 2:
            if board[x-1][y+1] == 2 or board[x+1][y+1] == 2:
                price += 500
            else:
                price += 100
        print(x,y,price)
        dfs(x-1,y,board,n,price)
        dfs(x+1,y,board,n,price)
        dfs(x,y-1,board,n,price)
        dfs(x,y+1,board,n,price)

        return price
    return price


def solution(board):

    answer = 0
    leng = len(board)
    # dfs go
    for x in range(leng):
        for y in range(leng):
            answer = dfs(x,y,board,leng,100)

    return answer

print(solution(board))