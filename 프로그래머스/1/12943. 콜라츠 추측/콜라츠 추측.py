def solution(num):
    answer = 0
    cnt =0
    while num !=1:
        if num ==1:
            answer =1
            break
        elif num %2 ==0:
            num = num //2
            cnt +=1
        else:
            num = num * 3 + 1
            cnt +=1
    if cnt >= 500:
        answer = -1
    elif cnt ==0:
        answer = 0
    else:
        answer = cnt
    return answer
        
    