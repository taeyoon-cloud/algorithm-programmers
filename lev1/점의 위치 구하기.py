def solution(dot):
    if dot[0] * dot[1] > 0:
        if dot[0] > 0:
            return 1
        else:
            return 3
    else:
        if dot[0] < 0:
            return 2
        else:
            return 4