def solution(i, j, k):
    answer = 0
    for num in range(i, j+1):
        num = str(num)
        answer += num.count(str(k))
    return answer