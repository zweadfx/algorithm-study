def solution(n):
    x = n ** 0.5
    answer = 0   
    if x==int(x):
        answer = (x+1)*(x+1)
    else:
        answer =-1
    return answer