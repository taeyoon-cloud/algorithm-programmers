def solution(s):
    answer = 0
    counts = dict()
    for c in s:
        if c not in counts.keys():
            if len(counts) == 0:
                x = c # 시작하는 수 x
            counts[c] = 1
        else:
            counts[c] += 1
            
        if counts[x] == sum(counts.values()) - counts[x]:
            answer += 1
            counts.clear()
            
    if len(counts) > 0:
        answer += 1
        
        
            
        
    return answer