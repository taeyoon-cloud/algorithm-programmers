def solution(my_string):
    answer = ""
    added_char = ""
    for c in my_string:
        if c in added_char:
            continue
        answer += c
        added_char += c
    
    return answer

def solution_1(my_string):
    answer = ""
    for c in my_string:
        if c not in answer:
            answer += c
    return answer
        