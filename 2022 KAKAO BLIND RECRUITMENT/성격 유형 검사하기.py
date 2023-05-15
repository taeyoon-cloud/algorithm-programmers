def solution(survey, choices):
    answer = ''

    check = {'R':0, 'T': 0, 'C':0, 'F': 0, 'J':0, 'M': 0, 'A':0, 'N': 0}
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    candidate = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for i in range(len(survey)):
        left, right = survey[i][0], survey[i][1]
        choice = choices[i]
        if choice >= 5:
            check[right] += score[choice]
        elif choice <= 3:
            check[left] += score[choice]

    for cand in candidate:
        if check[cand[0]] >= check[cand[1]]:
            answer += cand[0]
        else:
            answer += cand[1]
    
    return answer