def solution(s):
    answer = ''
    a = s.split(" ")
    for i in range(0, len(a)):
        for j in range(0, len(a[i])):
            if j%2 == 0:
                answer += a[i][j].upper()
            else:
                answer += a[i][j].lower()
        answer += " "
    return answer[:-1] # [:-1]을 해주지 않으면 문자 마지막에 공백이 들어간다...