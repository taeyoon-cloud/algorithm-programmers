from itertools import combinations

def solution(nums):
    arr = [True] * 50001 # 소수인지 아닌지 판단하기 위한 리스트 arr
    answer = 0
    
    candidates = list(combinations(nums, 3))
    candidates_sum = [sum(i) for i in candidates]
    maxim = max(candidates_sum)
    
    for i in range(2, int(maxim ** 0.5) + 1):
        j = 2
        while i * j <= maxim:
            if arr[i*j] == True:
                arr[i*j] = False
            j += 1
                
    for c in candidates_sum:
        if arr[c] == True:
            answer += 1
            
    return answer
    
    
    
    