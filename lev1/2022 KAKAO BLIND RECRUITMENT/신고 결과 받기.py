def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    
    # 아이디 별로 신고 당한 횟수를 저장하는 딕셔너리
    # key = 신고당한 아이디, value = 신고 당한 횟수
    reported_count = dict()
    
    # 아이디 별로 신고한 id를 저장하는 딕셔너리
    # key = 신고한 아이디, value = 신고 당한 아이디(들)
    reporter_who = dict()
    
    # 한 유저가 같은 유저를 여러 번 신고한 경우에는 신고 횟수 1회로 처리
    report = set(report)
    
    for line in report:
        reporter, reported = line.split()
        
        if reporter in reporter_who.keys():
            reporter_who[reporter].add(reported)
        else:
            reporter_who[reporter] = {reported}
            
        if reported in reported_count.keys():
            reported_count[reported] += 1
        else:
            reported_count[reported] = 1
            
    for i in range(len(id_list)):
        if id_list[i] not in reporter_who.keys():
            continue
        for report_id in reporter_who[id_list[i]]:
            if reported_count[report_id] >= k:
                answer[i] += 1
        
    return answer