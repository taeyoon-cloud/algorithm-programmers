def solution(age):
    arr = list(str(age))
    return "".join([chr(int(i) + 97) for i in arr])