def solution(sizes):
    # sizes = list(set(sizes)) # 중복 명함 제거 
    
    width_sorted_sizes = sorted(sizes, key = lambda x:-x[0])
    height_sorted_sizes = sorted(sizes, key = lambda x:-x[1])
    
    
    arr = []
    if width_sorted_sizes[0][0] > height_sorted_sizes[0][1]:
        for i in range(len(sizes)):
            arr.append(min(sizes[i]))
        return width_sorted_sizes[0][0] * max(arr)
    else:
        for i in range(len(sizes)):
            arr.append(min(sizes[i]))
        return height_sorted_sizes[0][1] * max(arr)
        