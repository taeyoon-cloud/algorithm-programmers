def solution(spell, dic):
    for word in dic:
        if len(word) == len(spell):
            if set(word) == set(spell):
                return 1
    return 2
        