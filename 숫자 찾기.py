def solution(num, k):
    answer = str(num).find(str(k)) + 1
    if answer == 0:
        answer = -1
    return answer