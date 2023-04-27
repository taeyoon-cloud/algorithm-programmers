def solution(n):
    num = 1 # 1, 3, 9, 27, 81 ....
    temp = '' # n을 3진법으로 변환한 수를 저장하는 변수
    
    while num * 3 <= n:
        num *= 3
        
    while num >= 1:
        temp += str(n//num)
        n %= num
        num //= 3
    
    
    answer = 0
    for index, i in enumerate(temp):
        answer += int(i) * (3 ** index)
    
    return answer
