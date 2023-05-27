from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    people = deque(people)
    
    while len(people) > 1:
        heavy = people[0]
        light = people[-1]
        if heavy + light <= limit:
            people.pop()
        
        people.popleft()
        answer += 1
    
    if len(people) == 1:
        return answer + 1
    else:
        return answer