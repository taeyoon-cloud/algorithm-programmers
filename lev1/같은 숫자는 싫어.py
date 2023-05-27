def solution(arr):
    temp = arr[0]
    result = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != temp:
            temp = arr[i]
            result.append(temp)
            
        
    
    return result


arr = [1, 2, 3, 4, 5]
print(arr[-2:])
        
        