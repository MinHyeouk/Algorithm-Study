def solution(s):
    a = s.lower()
    if len(a) == 0:
        return True
    elif a.count('p') == a.count('y'):
        return True
    else:
        return False