def solution(quiz):
    answer = []
    for q in quiz:
        line = list(q.split())
        if line[1] == '+':
            if int(line[0]) + int(line[2]) == int(line[4]):
                answer.append("O")
            else:
                answer.append("X")
                
        else:
            if int(line[0]) - int(line[2]) == int(line[4]):
                answer.append("O")
            else:
                answer.append("X")
        
                
    return answer