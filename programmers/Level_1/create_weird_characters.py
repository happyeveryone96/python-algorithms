def solution(s):
    answer = []
    cnt = 0
    for i in range(len(s)):
        if (s[i] == ' '):
            cnt = 0
            answer.append(' ')
        elif (cnt % 2 == 0 and s[i] != ' '):
            answer.append((s[i]).upper())
            cnt += 1
        else:
            answer.append((s[i]).lower())
            cnt += 1
    answer = ''.join(answer)
    return answer
