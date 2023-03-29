from itertools import permutations

def solution(babbling):
    answer = 0
    can_speak_word = ["aya", "ye", "woo", "ma"]
    can_speak_words = []
    for i in range(1, 5):
        results = list(permutations(can_speak_word, i))
        for result in results:
            can_speak_words.append("".join(result))
            
    print(can_speak_words)
        
    for babbl in babbling:
        if babbl in can_speak_words:
            answer += 1
            
        

    return answer