def solution(number, limit, power):
    arr = [0 for i in range(number+1)] # 약수의 개수를 저장하는 리스트
    
    for i in range(1, number+1):
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                arr[i] += 1
        if i ** 0.5 == int(i**0.5):# 제곱수인 경우
            arr[i] = arr[i] * 2 - 1
        else:
            arr[i] = arr[i] * 2
            
                
    for i in range(1, number + 1):
        if arr[i] > limit:
            arr[i] = power
            
    return sum(arr)