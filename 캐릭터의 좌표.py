def solution(keyinput, board):
    n = board[1] # 세로 크기
    m = board[0] # 가로 크기
    
    commands = ["up", "down", "left", "right"]
    dx = [0 ,0, -1, 1]
    dy = [1, -1, 0, 0]
    x = 0
    y = 0
    
    for key in keyinput:
        i = commands.index(key)
        nx = x + dx[i]
        ny = y + dy[i]
        if abs(nx) <= m//2:
            x = nx
        if abs(ny) <= n//2:
            y = ny
    
    return [x, y]
        