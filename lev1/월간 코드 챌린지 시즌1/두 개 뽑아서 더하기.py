from itertools import combinations

def solution(numbers):
    candidates = list(combinations(numbers, 2))
    answer = sorted(list(set([sum(i) for i in candidates])))
    
    return answer