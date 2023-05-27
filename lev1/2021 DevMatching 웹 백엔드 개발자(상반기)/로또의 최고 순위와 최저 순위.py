def solution(lottos, win_nums):
    ranks = [6, 6, 5, 4, 3, 2, 1] # index만큼 번호가 일치하면 ranks[index]가 순위가 됨
    answer = []
    
    if 0 not in lottos: # 구매한 로또 번호에 0이 없는 경우
        match_num = len(set(lottos)&set(win_nums))
        answer.append(ranks[match_num])
        answer.append(ranks[match_num])
    
    else:
        least_match_num = len(set(lottos)&set(win_nums))
        count_zero = lottos.count(0)
        answer.append(ranks[least_match_num + count_zero])
        answer.append(ranks[least_match_num])
        
    return answer