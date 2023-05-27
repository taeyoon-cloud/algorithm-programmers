from itertools import combinations

def solution(number):
    count = 0
    candidates = list(combinations(number, 3))
    
    for cand in candidates:
        if sum(cand) == 0:
            count += 1
            
    return count
    