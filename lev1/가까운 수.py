def solution(array, n):
    answer = 0
    maxim = 101
    for num in array:
        temp = abs(num-n)
        if temp < maxim:
            maxim = temp
            answer = num
        elif temp == maxim:
            answer = min(answer, num)
            
    return answer


def solution_1(array, n):
    array.sort(key = lambda x: (abs(x-n), x-n))
    return array[0]