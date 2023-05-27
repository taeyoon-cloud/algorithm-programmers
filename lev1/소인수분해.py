def solution(n):
    temp = 2
    answer = set()
    while n > 1:
        while n % temp == 0:
            n //= temp
            answer.add(temp)
        temp += 1

    return sorted(list(answer))