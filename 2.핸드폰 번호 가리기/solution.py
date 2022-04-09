def solution(phone_number):
    a = len(phone_number)
    b = phone_number[-4:]
    return '*'*(a-4) + b