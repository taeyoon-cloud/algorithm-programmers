def solution(players, callings):
    players_dict = {}
    for i in range(len(players)):
        players_dict[players[i]] = i  # {"mumu": 0} 이런 형태로 dictionary 생성
        
    for call in callings:
        call_index = players_dict[call] # call_index = 해설자가 부른 선수의 index
        
        players_dict[players[call_index - 1]] = call_index # 해설자가 부른 선수 바로 앞에 있는 선수의 index를 해설자가 부른 선수의 index로 변경
        players_dict[call] = call_index - 1 # 해설자가 부른 선수의 index를 바로 앞으로 변경
        
        
        players[call_index], players[call_index-1] = players[call_index-1], players[call_index]
        # 해설자가 선수를 부를 때마다, 양 선수 위치 변경
        
    return players
        

        
        
        