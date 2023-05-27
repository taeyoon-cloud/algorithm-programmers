def solution(n):
    arr = [1]
    for i in range(1, 11):
        arr.append(i * arr[i-1])
        
    for i in range(1, 11):
        if n >= arr[i]:
            answer = i
        if n < arr[i]:
            break
    return answer
    
    