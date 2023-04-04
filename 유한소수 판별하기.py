import math

def solution(a, b):
    gcd = math.gcd(a, b)
    b //= gcd
    
    li = []
    i = 2
    while i <= b:
        if b % i == 0:
            li.append(i)
            b //= i
        else:
            i += 1
        
    if all(i in [2, 5] for i in li):
        return 1
    return 2



def solution_1(a, b):
    gcd = math.gcd(a, b)
    b //= gcd
    
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    if b == 1:
        return 1
    return 2