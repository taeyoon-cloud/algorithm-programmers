def solution(n):
    numbers = [0]
    i = 1
    while len(numbers) <= 100:
        if '3' not in str(i) and i%3 != 0:
            numbers.append(i)
        i += 1
            
    return numbers[n]