def solution(price, money, count):
    total = 0
    for i in range(1, count + 1):
        total += price * i
    
    answer = 0 if total <= money else total - money
    return answer