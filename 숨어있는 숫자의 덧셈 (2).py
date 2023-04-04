def solution(my_string):
    numbers = [str(i) for i in range(10)]
    
    temp = ""
    answer = 0
    for c in my_string:
        if c in numbers:
            temp += c
        else:
            if temp != "":
                answer += int(temp)
                temp = ""
    
    if temp != "":
        answer += int(temp)
        
    return answer