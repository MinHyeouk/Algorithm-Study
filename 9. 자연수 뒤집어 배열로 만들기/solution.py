def solution(n):
    a = str(n)
    b = list(a)
    c = b[::-1]
    d =  [int(i) for i in c]
    return d

    # map 과 reversed를 이용하여
    # list(map(int, reversed(str(n)))) 로 해결 가능