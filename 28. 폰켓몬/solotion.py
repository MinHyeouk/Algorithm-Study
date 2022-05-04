def solution(nums):
    answer = 0
    a = len(nums)//2
    b = list(set(nums))
    for i in b:
        if answer < a:
            answer += 1
    return answer