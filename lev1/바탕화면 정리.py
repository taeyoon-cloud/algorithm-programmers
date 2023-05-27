def solution(wallpaper):
    answer = []
    candidates_x = set()
    candidates_y = set()
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                candidates_x.add(i)
                candidates_y.add(j)
    
    answer.append(min(candidates_x))
    answer.append(min(candidates_y))
    answer.append(max(candidates_x) + 1)
    answer.append(max(candidates_y) + 1)
    
    return answer