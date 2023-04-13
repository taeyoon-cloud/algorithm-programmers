def solution(n, arr1, arr2):
    answer_list = [] # 정답을 저장하는 리스트
    length = len(arr1) # 행, 열 개수
    for i in range(length):
        answer = "" # 각 행에서의 암호화된 배열
        row1 = arr1[i]
        row2 = arr2[i]
        j = 2 ** (length - 1) # 2^n-1 ~ 1까지 확인한다.
        while j >= 1:
            if row1 // j == 1 or row2 // j == 1: # 지도1, 지도 2 둘중 하나라도 벽이라면
                answer += "#" # answer에 # 추가
                if row1 // j == 1: # 만약 나눠진다면, row값을 나눈 나머지로 바꾼다.
                    row1 %= j
                if row2 // j == 1:
                    row2 %= j           
            else: # 지도 1, 지도 2 둘다 벽이 아니라면 공백 추가
                answer += " "

            j //= 2
            
        answer_list.append(answer)
        
    return answer_list