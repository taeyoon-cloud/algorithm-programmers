def solution(cards1, cards2, goal):
    index1 = 0
    index2 = 0
    
    for word in goal:
        # goal의 원소가 cards1에 있는 경우
        if word in cards1:
            # 카드를 사용하는 경우, index1을 다음 카드 번호로 초기화
            if cards1.index(word) == index1: 
                index1 = cards1.index(word) + 1
            # 카드를 사용하지 않고 다음 카드를 넘어갈 수 없으므로
            else:
                return "No"
                 
        # goal의 원소가 cards2에 있는 경우
        else:
            if cards2.index(word) == index2:
                index2 = cards2.index(word) + 1
            else:
                return "No"
    
    
    return "Yes"
            
        