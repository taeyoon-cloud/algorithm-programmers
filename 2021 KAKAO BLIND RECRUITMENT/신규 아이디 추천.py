def solution(new_id):
    dict = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", '-', '_', '.'}
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    new_id = list(new_id)
    for i in range(len(new_id)):
        if new_id[i]  not in dict:
            new_id[i] = ' '
    new_id = "".join(new_id).replace(" ", "")
    
    
    # 3단계
    temp = ""
    new_id = list(new_id)
    for c in new_id:
        if c == '.' and len(temp) >= 1:
            if temp[-1] == '.':
                continue
            else:
                temp += c
        else:
            temp += c
    
    new_id = temp
    
            
    # 4단계
    
    if new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    
        
    # 5단계
    if new_id == '':
        new_id += 'a'
        
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:-1]
    
    # 7단계
    if len(new_id) <= 2:
        temp = new_id[-1]
        while len(new_id) < 3:
            new_id += temp
            
    
            
    return new_id