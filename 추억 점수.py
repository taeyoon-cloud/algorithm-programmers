def solution(name, yearning, photo):
    yearning_dict = {}
    result = []
    # yearning_dict에 이름:그리움 점수로 저장
    # 그리움 점수가 없을 경우 0으로 저장
    for i in range(len(name)):
        if i < len(yearning):
            yearning_dict[name[i]] = yearning[i]
        else:
            yearning_dict[name[i]] = 0
            

    # 사진 속 사람이 name 리스트에 있는 경우, 해당 그리움 점수를 더함
    # 없는 경우, 패스
    for p in photo:
        temp_result = 0
        for person in p:
            if person in name:
                temp_result += yearning_dict[person]
            else:
                continue
        result.append(temp_result)
    
    return result
                
        