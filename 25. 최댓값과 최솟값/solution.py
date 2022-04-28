def solution(s):
    a = list(s.split(' '))
    b = list(map(int, a))
    c = min(b)
    d = max(b)
    e = [c,d]
    f = list(map(str, e))
    g = ' '.join(f)
    return g

    # s = list(map(int, s.split()))
    # return str(min(s)) + " " + str(max(s))
    # 생각을 하자 !