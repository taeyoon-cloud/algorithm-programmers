def solution(array):
    answer = 0
    for num in array:
        answer += str(num).count('7')
    return answer

def solution_1(array):
    return str(array).count('7')