is_prime = [True for _ in range(101)] # 0제외하고 index로 1~100까지 확인하기 위해서

def eratos():
    for i in range(2, 11):
        if is_prime[i]:
            for j in range(i*2,101,i):
                is_prime[j] = False
        

def solution(n):
    eratos()
    return is_prime[1:n+1].count(False)