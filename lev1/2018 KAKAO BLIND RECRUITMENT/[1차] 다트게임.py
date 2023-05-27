def solution(dartResult):
    darts = []
    j = 0
    for i in range(2, len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[j:i] == '1':
                continue
            darts.append(dartResult[j:i])
            j = i
    darts.append(dartResult[j:])
    
    total = 0
    darts = [list(dart) for dart in darts]
    
    for i in range(3):
        if darts[i][0] == '1' and darts[i][1] == '0':
            darts[i] = ['10', darts[i][2]]
    
    
    score = [0, 0, 0]
    
    # 계산식 시작
    for i in range(3):
        if darts[i][1] == 'S':
            score[i] += int(darts[i][0])
        elif darts[i][1] == 'D':
            score[i] += int(darts[i][0]) ** 2
        else:
            score[i] += int(darts[i][0]) ** 3
        
        if len(darts[i]) == 3: # *나 #가 있는 경우
            if darts[i][2] == '*': # *(스타상)
                if i == 0:
                    score[i] *= 2
                else:
                    score[i] *= 2
                    score[i-1] *= 2
            else: # #(아차상)
                score[i] *= -1
                
    print(score)
    return sum(score)
                    
            