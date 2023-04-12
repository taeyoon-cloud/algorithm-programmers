def solution(n):
    arr = [True] * 100
    
    for i in range(2, int((n ** 0.5)) + 1):
        j = 2
        while i * j <= n:
            print(i, j)
            if arr[i*j] == True:
                arr[i*j] == False
            j += 1
            
    print(arr)
    
    return arr[2:n+1].count(True)


print(solution(10))