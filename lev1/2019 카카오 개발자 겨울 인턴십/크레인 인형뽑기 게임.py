def solution(board, moves):
    answer = 0 # 사라진 인형의 개수
    backet = [] # 뽑은 인형을 저장하는 바구니 리스트
    n = len(board) # 게임 화면의 길이
    
    for move in moves:
        move -= 1
        for i in range(n):
            if board[i][move] != 0: # 해당 칸에 인형이 있다면 
                backet.append(board[i][move]) # 바구니에 추가
                board[i][move] = 0
                break
        if len(backet) > 1:
            if backet[-1] == backet[-2]: # 같은 인형이 들어간 경우
                backet = backet[:-2] # 바구니에서 인형 2개 제거
                answer += 2
        
    return answer