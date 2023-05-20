def solution(n, m, section):
    answer = 0
    
    end = 0 # 페인트를 칠한 끝부분 영역의 번호
    for sect in section:
        if sect <= end: # 만약 sect가 이미 칠해졌다면 continue를 통해 다음 구역으로 넘어감
            continue
        else: # sect가 아직 칠해지지 않았으므로 끝부분 영역의 번호를 다시 초기화 후 칠한 횟수 + 1
            end = sect + m - 1
            answer += 1
            
            
    return answer