def solution(s):
    answer = []
    if len(s) % 2 == 0:
        answer.extend([s[int((len(s))/2-1)], s[int((len(s))/2)]])
    else:
        answer.append(s[int((len(s)-1)/2)])
    answer = ''.join(answer)
    return answer
