def solution(a, b):
    results = ["FRI","SAT", "SUN","MON","TUE","WED","THU"]
    date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    sum_date = sum(date[:a]) + b
    
    return results[(sum_date-1) % 7]