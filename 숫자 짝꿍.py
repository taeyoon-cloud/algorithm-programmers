from collections import Counter
from itertools import permutations

def solution(X, Y):
    answer = ''
    
    x = Counter(X)
    y = Counter(Y)
    
    set_x = set(Counter(X).keys())
    set_y = set(Counter(Y).keys())
    common = set_x & set_y
    
    if len(common) == 0:
        return "-1"
    
    candidates = []
    
    for cand in common:
        if x[cand] < y[cand]:
            for i in range(int(x[cand])):
                candidates.append(cand)
        else:
            for i in range(int(y[cand])):
                candidates.append(cand)
                
    # 중복되는 원소가 한 종류일 경우
    if len(set(candidates)) == 1:
        return candidates[0]
            
    # 중복되는 원소가 여러 종류일 경우 -> 제일 큰 정수 찾기
    candidates.sort(reverse = True)
    answer = "".join(candidates)
    
    
    return answer