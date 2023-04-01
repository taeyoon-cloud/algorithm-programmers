def solution(n):
    total = 0
    answer = str(n)
    for num in answer:
        total  += int(num)
    return total

def solution_1(n):
    return sum(list(map(int, list(str(n)))))