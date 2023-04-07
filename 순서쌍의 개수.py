import math
def solution(n):
    total = 0
    temp = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += 1
            temp = i
    if temp ** 2 == n:
        return total * 2 - 1
    return total * 2