def solution(board):
    n = len(board)
    large_map = [[0 for _ in range(n+2)] for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            large_map[i+1][j+1] = board[i][j]
            
    for i in range(1, n+1):
        for j in range(1, n+1):
            if large_map[i][j] == 1:
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if large_map[k][l] != 1:
                            large_map[k][l] = 2
             

    answer = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if large_map[i][j] == 0:
                answer += 1
            
            
            
    return answer


def solution_1(board):
    n = len(board)
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    
    boom = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                boom.append((i, j))
    
    for x, y in boom:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
                
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer
        
                    
                    