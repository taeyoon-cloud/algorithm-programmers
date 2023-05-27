def solution(score):
    answer = []
    average = [sum(s)/2 for s in score]
    average_rank = sorted(average, reverse = True)
    
    for num in average:
        answer.append(average_rank.index(num) + 1)
    return answer