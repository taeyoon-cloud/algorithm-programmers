def solution(s):
    answer = []
    answer_set = set()
    
    for i in range(len(s)):
        if s[i] not in answer_set:
            answer_set.add(s[i])
            answer.append(-1)
        else:
            temp = 1
            j = i-1
            while s[i] != s[j]:
                temp += 1
                j -= 1
            answer.append(temp)
                
    
    return answer