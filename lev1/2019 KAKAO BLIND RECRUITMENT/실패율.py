from collections import Counter

def solution_2(N, stages):
    answers = [[0,10]]
    fail_counts = Counter(stages)
    fail_counts_list = list(zip(fail_counts.keys(), fail_counts.values()))
    fail_rates = [[i, 0, 0] for i in range(N+1)] 
    # [a, b, c] = [a번 스테이지, 스테이지에 도달했지만 아직 클리어하지 못한 플레이어 수, 스테이지에 도달한 플레이어 수]

    
    for i in range(1, N+1):
        fail_rates[i][1] = fail_counts[i] # 스테이지에 도달했지만 아직 클리어하지 못한 플레이어의 수
        fail_rates[i][2] = sum([count[1] for count in fail_counts_list if count[0] >= i])
        # 스테이지에 도달한 플레이어의 수
        

        
        if fail_rates[i][2] == 0: # 스테이지에 도달한 플레이어의 수가 없는 경우 실패율은 0
            answers.append([i,0])
        else:
            answers.append([i,fail_rates[i][1] / fail_rates[i][2]])
            
        
    answers.sort(key = lambda x: (-x[1], x[0]))
    return [answer[0] for answer in answers[1:]]


from collections import Counter

def solution_1(N, stages):
    answers = [[0,10]]
    fail_counts = Counter(stages)
    fail_counts_list = list(zip(fail_counts.keys(), fail_counts.values()))

    for i in range(1, N+1):
        notclear_player = fail_counts[i] # 스테이지에 도달했지만 아직 클리어하지 못한 플레이어의 수
        reached_player = sum([count[1] for count in fail_counts_list if count[0] >= i])
        # 스테이지에 도달한 플레이어의 수
        
        if reached_player == 0: # 스테이지에 도달한 플레이어의 수가 없는 경우 실패율은 0
            answers.append([i,0])
        else:
            answers.append([i,notclear_player / reached_player])
            
        
    answers.sort(key = lambda x: (-x[1], x[0]))
    return [answer[0] for answer in answers[1:]]