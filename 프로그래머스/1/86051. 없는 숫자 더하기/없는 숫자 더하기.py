def solution(numbers):
    answer = 0
    l = len(numbers)
    for i in range(10):
        if i not in numbers:
            answer+=i
    return answer