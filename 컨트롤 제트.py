def solution(s):
    arr = list(s.split())
    
    total = 0
    temp = 0
    for i in range(len(arr)):
        if arr[i] == 'Z':
            total -= temp
        else:
            temp = int(arr[i])
            total += temp
            
    return total