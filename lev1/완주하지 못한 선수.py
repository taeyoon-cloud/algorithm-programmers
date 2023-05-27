# 마지막 효율성 테스트 시간 초과 나는 코드
def solution(participant, completion):
    participant_dict = {}
    completion_dict = {}
    
    # 완주 못한 사람이 동명이인이 아닐 경우
    temp = list(set(participant) - set(completion))
    if temp != []:
        return temp[0]
        
        
    # 완주 못한 사람이 동명이인일 경우
    for p in participant:
        if p in list(participant_dict.keys()):
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1
            
    arr = [i for i in list(participant_dict.keys()) if participant_dict[i] >= 2]
            
    for c in completion:
        if c in list(completion_dict.keys()):
            completion_dict[c] += 1
        else:
            completion_dict[c] = 1
            
            
    for key in arr:
        if participant_dict[key] != completion_dict[key]:
            return key
        


# colection 라이브러리 사용
import collections

def solution(participant, completion):
    count = collections.Counter(participant) - collections.Counter(completion)
    return list(count.keys())[0]
        


            