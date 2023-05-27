def solution(polynomial):
    polys = list(polynomial.split("+"))
    polys = [i.strip() for i in polys]
    
    poly = 0
    num = 0
    
    for i in polys:
        if 'x' in i:
            if i == 'x':
                poly += 1
            else:
                poly += int(i[:-1])
        else:
            num += int(i)
            
    answer = ""
    if poly == 0:
        if num != 0:
            return str(num)
        else:
            return "0"
    elif poly == 1:
        answer += "x"
    else:
        answer += str(poly)
        answer += "x"
    
    if num != 0:
        answer +=" + "
        answer += str(num)
    return answer