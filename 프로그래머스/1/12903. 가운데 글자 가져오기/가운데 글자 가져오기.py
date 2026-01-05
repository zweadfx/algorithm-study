def solution(s):
    answer = ''
    s_len = len(s)
    half = s_len/2
    if s_len %2==0:
        answer = s[int(half-1):int(half+1)]
    else:
        answer = s[int(half):int(half+1)]
    return answer