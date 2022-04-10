def solution(n):
    a = str(n)
    b = list(a)
    c = list(map(int, b))
    d = sum(c)
    return d

    # return sum(map(int,str(n))) 으로 한방에 해결 가능하다...