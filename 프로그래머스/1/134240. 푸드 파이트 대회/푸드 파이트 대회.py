def solution(food):
    answer = ''
    an = ''
    l=len(food)
    for i in range(1,l):
        an += str(i) * (food[i]//2)
    answer = an + str(0)+ an[::-1]
    return answer