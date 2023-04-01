import math

def solution(n):
    answer = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n//i)
            
    return sorted(list(answer))


def solution_1(n):
    answer = [i for i in range(1,n+1) if n%i == 0]
    return answer