from collections import deque

def solution(numbers, direction):
    q = deque(numbers)
    if direction == "right":
        q.appendleft(q.pop())
    else:
        q.append(q.popleft())
        
    return list(q)
        

def solution_1(numbers, direction):
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else:
        return numbers[1:] + [numbers[0]]
        
        