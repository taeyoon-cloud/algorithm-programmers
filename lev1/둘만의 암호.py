def solution(s, skip, index):
    answer = ''
    
    skip = set(map(ord, skip))
    
    for c in s:
        changed = ord(c)
        temp = 0
        while temp < index:
            changed += 1
            if changed == 123:
                changed -= 26
            if changed not in skip:
                temp += 1               
        
        answer += chr(changed)
                    
        
        
    
    return answer