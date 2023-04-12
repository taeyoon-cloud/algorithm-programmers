def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for c in s:
        if c.isdigit():
            continue
        else:
            return False
    return True
