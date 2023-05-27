def solution(babbling):
    babbling_list = ["aya", "ye", "woo", "ma"]
    answer =  0
    for babb in babbling:
        for babb_dict in babbling_list:
            if babb_dict * 2 not in babb:
                babb = babb.replace(babb_dict, " ")

        if babb.strip() == "":
            answer += 1
                
    return answer