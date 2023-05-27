def solution(park, routes):
    len_x = len(park) # 세로 길이
    len_y = len(park[0]) # 가로 길이
    
    # E, W, S, N
    direct = {"E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0]}
    
    # 출발지 지정
    for i in range(len_x):
        for j in range(len_y):
            if park[i][j] == "S":
                x = i
                y = j
                break
                
    for r in routes:
        op, dist = r.split()
        op = direct[op]
        dist = int(dist)
        
        dx, dy = op[0], op[1] # 방향

        nx = x + dx * dist
        ny = y + dy * dist

        if nx < 0 or nx >= len_x or ny < 0 or ny >= len_y:
            continue

        if nx >= x:
            if 'X' in [park[i][y] for i in range(x, nx+1)]:
                continue
        else:
            if 'X' in [park[i][y] for i in range(nx, x+1)]:
                continue

        if ny >= y:
            if 'X' in park[x][y:ny+1]:
                continue
        else:
            if 'X' in park[x][ny:y+1]:
                continue


        x = nx
        y = ny

        

        print(x, y)


 

        
                
            
                

# solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])
# solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])
solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])