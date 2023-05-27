import math

def solution(numer1, denom1, numer2, denom2):
    denom = (denom1 * denom2) // math.gcd(denom1, denom2)
    numer = numer1 * (denom // denom1) + numer2 * (denom // denom2)
    
    divisor = math.gcd(denom, numer)
    return [numer // divisor, denom // divisor]