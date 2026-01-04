def solution(phone_number):
    hide = len(phone_number)-4
    star = '*'* hide
    tail = phone_number[-4:]
    
    answer = star+tail
    return answer