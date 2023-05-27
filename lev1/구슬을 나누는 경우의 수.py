# from itertools import combinations

# # 시간 초과
# def solution(balls, share):
#     return (len(list(combinations(range(balls), share))))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

def solution(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls-share))




import math

def solution_1(balls, share):
    return math.comb(balls, share)
    
    