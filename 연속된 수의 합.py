def solution(num, total):
    
    mid = total // num
    start = mid - (num-1) // 2
    end = mid + (num-1) // 2
    
    if num % 2 == 0:
        end += 1
    
    answer = [i for i in range(start, end+1)]
    
    return answer