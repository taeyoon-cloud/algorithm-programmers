def solution(dots):
    answer = 0
    i = 0
    for j in range(i+1, 3):
        first_gradient = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
        second_gradient = (dots[3-i][1] - dots[3-j][1]) / (dots[3-i][0] - dots[3-j][0])
        if first_gradient == second_gradient:
            answer  = 1
            break
    i = 0
    j = 3
    first_gradient = (dots[i][1] - dots[j][1]) / (dots[i][0] - dots[j][0])
    second_gradient = (dots[1][1] - dots[2][1]) / (dots[1][0] - dots[2][0])
    if first_gradient == second_gradient:
        answer  = 1
    
    return answer