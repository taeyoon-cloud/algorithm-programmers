def solution(emergency):
    emer_sort = sorted(emergency, reverse = True)
    answer = []
    
    for num in emergency:
        answer.append(emer_sort.index(num) + 1)
    return answer