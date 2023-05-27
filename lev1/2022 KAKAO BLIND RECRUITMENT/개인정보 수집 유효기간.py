def solution(today, terms, privacies):
    answer = []
    
    year_today, month_today, date_today = map(int, today.split("."))
    sum_date_today = year_today * 336 + month_today * 28 + date_today
    
    terms_dict = dict()
    for term in terms:
        alpha, duration = term.split()
        terms_dict[alpha] = int(duration)
    
    for i in range(len(privacies)):
        full_date, term = privacies[i].split()
        year, month, date = map(int, full_date.split("."))
        
        month += terms_dict[term]
        sum_date_privacy = year * 336 + month * 28 + date
        
        if sum_date_today >= sum_date_privacy:
            answer.append(i+1)
              
    return answer