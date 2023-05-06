def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    boxes = []
    for i in range(len(score) // m):
        boxes.append(score[m*i:m*(i+1)])
        
    for box in boxes:
        answer += box[m-1] * m
        
    return answer
        