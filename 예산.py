def solution(d, budget):
    d.sort()
    total = 0 # 현재까지의 지원 금액
    answer = 0 # 최대로 지원할 수 있는 부서의 수
    for money in d:
        budget -= money
        if budget < 0:
            break
        answer += 1
            
    return answer
        