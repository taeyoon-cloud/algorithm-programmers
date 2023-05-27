def solution(dots):
    set_x = list(set([i[0] for i in dots]))
    set_y = list(set([i[1] for i in dots]))
    
    return abs(set_x[1] - set_x[0]) * abs(set_y[1] - set_y[0])