def solution(my_string):
    line = my_string.split()
    total = int(line[0])
    for i in range(1, len(line), 2):
        if line[i] == "+":
            total += int(line[i+1])
        else:
            total -= int(line[i+1])
    
    return total