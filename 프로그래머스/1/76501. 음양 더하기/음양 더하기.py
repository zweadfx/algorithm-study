def solution(absolutes, signs):
    answer = 0
    l=len(absolutes)
    for i in range(0, l):
        if signs[i] == True:
            answer += absolutes[i]
        elif signs[i] == False:
            answer += -absolutes[i]   
    return answer