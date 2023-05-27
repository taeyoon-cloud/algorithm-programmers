def solution(n, lost, reserve):
    clothes = [1] * (n+1) # 0번 인덱스는 제외
    for l in lost:
        clothes[l] -= 1
    for r in reserve:
        clothes[r] += 1
        
    lost.sort()
    reserve.sort()
    
    for l in lost:
        if clothes[l] == 0:
            if l == 1:
                if clothes[l+1] == 2:
                    clothes[l] += 1
                    clothes[l+1] -= 1
            elif l == n:
                if clothes[l-1] == 2:
                    clothes[l] += 1
                    clothes[l-1] -= 1
            else:
                if clothes[l-1] == 2:
                    clothes[l] += 1
                    clothes[l-1] -= 1
                elif clothes[l+1] == 2:
                    clothes[l] += 1
                    clothes[l+1] -= 1
            
    print(clothes)
    return len([i for i in clothes[1:] if i >= 1])
            