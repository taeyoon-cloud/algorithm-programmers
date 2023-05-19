def solution(keymap, targets):
    result = []
    
    keymap = set(keymap) # 탐색 시간 감소를 위해 set 자료형으로 변경
    
    keymap_dict = dict() # 각 문자별 최소로 눌러야 할 숫자를 저장할 dictionary
    for target in targets:
        answer = 0 # 각 target별 최소로 눌러야 하는 숫자
        for c in target:
            if c in keymap_dict.keys():
                answer += keymap_dict[c]
            
            # keymap_dict에 해당 문자가 있는 경우, 가장 적게 키패드를 누르는 수를 dictionary에 추가하고
            # 없는 경우, result에 -1 추가
            else:
                location = 1000
                for key in keymap:
                    temp = key.find(c)
                    if temp != -1:
                        location = min(temp, location)
                if location == 1000:
                    answer = -1
                    break
                else:
                    keymap_dict[c] = location + 1
                    answer += keymap_dict[c]
                    

        result.append(answer)
                    
                
    return result