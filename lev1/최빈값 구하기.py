def solution(array):
    arr_set = set(array)
    answers = []
    for num in arr_set:
        answers.append((num, array.count(num)))
    
    answers.sort(key=lambda x: -x[1])
    
    print(answers)
    
    if len(answers) != 1:
        if answers[0][1] == answers[1][1]:
            return -1
        else:
            return answers[0][0]
    else:
        return answers[0][0]
    
    