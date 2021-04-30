
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


def solution(board, moves):
    leng = len(board)
    moves = [(i - 1) for i in moves]
    
    board_stack = [[] for _ in range(leng)]
    
    # get last index each stack
    for i in range(leng):

        for j in range(leng-1,-1,-1):
            if board[j][i] != 0:
                board_stack[i].append(board[j][i])
    res_stack = []
    answer = 0
    for move in moves:
        if len(board_stack[move]) == 0:
            continue
        get_sticker = board_stack[move].pop()
        res_stack.append(get_sticker)
        
        if len(res_stack) > 1: 
            if get_sticker == res_stack[-2]:
                res_stack.pop()
                res_stack.pop()
                answer += 2
        
    return answer

print(solution(board,moves))