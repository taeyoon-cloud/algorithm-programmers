import math

def solution(n):
    answer = 1 if math.sqrt(n) == int(math.sqrt(n)) else 2
    return answer