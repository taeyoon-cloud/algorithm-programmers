def solution(common):
    answer = 0
    target_index = len(common)
    add = common[1] - common[0]
    if common[0] != 0: # common[0]가 0이 아닌 경우에만 나눌 수 있다.
        multiply = common[1] // common[0]
    
    
    if add == common[2] - common[1]:
        answer = common[0] + add * target_index
    
    elif multiply == common[2] // common[1]: #  
        answer = common[0]
        for i in range(target_index):
            answer *= multiply
    
    
    return answer




def solution_1(common):
    answer = 0
    if common[2] - common[1] == common[1] - common[0]:
        answer = common[-1] + (common[1] - common[0])
    else:
        answer = common[-1] * (common[1] // common[0])
    
    return answer