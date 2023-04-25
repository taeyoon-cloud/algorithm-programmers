def solution(numbers, hand):
    answer = ''
    keypads = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    left_finger = keypads[3][0] # 왼손의 위치
    right_finger = keypads[3][2] # 오른손의 위치
    
    for n in numbers:
        n = str(n)
        # n이 1, 4, 7인 경우
        if n == '1' or n == '4' or n == '7':
            left_finger = n
            answer += 'L'
        # n이 3, 6, 9인 경우
        elif n == '3' or n == '6' or n == '9':
            right_finger = n
            answer += 'R'    
        # n이 2, 5, 8, 0인 경우
        else:
            for i in range(4):
                for j in range(3):
                    if keypads[i][j] == right_finger:
                        right_i, right_j = i, j
                    if keypads[i][j] == left_finger:
                        left_i, left_j = i, j
                    if keypads[i][j] == n:
                        target_i, target_j = i, j
            
            dist_left = abs(left_i - target_i) + abs(left_j - target_j)
            dist_right = abs(right_i - target_i) + abs(right_j - target_j)
            
            if dist_left < dist_right:
                left_finger = n
                answer += 'L'
            elif dist_left == dist_right:
                if hand == 'left':
                    left_finger = n
                    answer +='L'
                else:
                    right_finger = n
                    answer += 'R'
            else:
                right_finger = n
                answer += 'R'
        
    
    return answer