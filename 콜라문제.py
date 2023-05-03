def solution(a, b, n):
    count = 0
    while n >= a:
        temp = (n // a)
        new_bottle = temp * b
        empty_bottle = temp * a
        n = n - empty_bottle + new_bottle
        count += new_bottle
        
    return count