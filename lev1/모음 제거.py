def solution(my_string):
    answer = ""
    for s in my_string:
        if s in ['a', 'e', 'i', 'o', 'u']:
            continue
        answer += s
    return answer

def solution_1(my_string):
    return "".join([s for s in my_string if s not in 'aeiou'])