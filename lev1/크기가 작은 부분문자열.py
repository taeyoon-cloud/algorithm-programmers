def solution(t, p):
    len_p = len(p)
    len_t = len(t)
    answer = 0
    
    for i in range(len_t - len_p + 1):
        substring = t[i:i+len_p]
        if int(substring) <= int(p):
            answer += 1
            
    return answer