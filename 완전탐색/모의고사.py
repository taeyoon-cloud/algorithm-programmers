def solution(answers):
    n = len(answers)
    stu1 = [1,2,3,4,5] * (n // 5 + 1)
    stu1 = stu1[:n]
    stu2 = [2,1,2,3,2,4,2,5] * (n // 8 + 1)
    stu2 = stu2[:n]
    stu3 = [3,3,1,1,2,2,4,4,5,5] * (n // 10 + 1)
    stu3 = stu3[:n]
    
    
    count = [0, 0, 0]
    for i in range(n):
        if answers[i] == stu1[i]:
            count[0] += 1
        if answers[i] == stu2[i]:
            count[1] += 1
        if answers[i] == stu3[i]:
            count[2] += 1
            
            
    # 가장 문제를 많이 맞힌 사람을 저장하는 리스트
    answer = []
    for i in range(3):
        if count[i] == max(count):
            answer.append(i+1)
            
    return answer
            
    
    
    
    