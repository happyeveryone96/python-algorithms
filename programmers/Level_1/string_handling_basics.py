def solution(s):
    if s.isdigit() == True and (len(s) == 4 or len(s) == 6):
        answer = True
        for i in range(len(s)):
            if s[i] == 'e':
                answer = False
    else:
        answer = False
    return answer
