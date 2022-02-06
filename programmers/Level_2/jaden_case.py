def solution(s):
    answer = []
    whitespace = 0
    for i in range(len(s)):
        if i == 0:
            answer.append(s[i].upper())
        elif s[i] == ' ':
            answer.append(s[i])
            whitespace += 1
        elif s[i] != ' ' and whitespace > 0:
            answer.append(s[i].upper())
            whitespace = 0
        else:
            answer.append(s[i].lower())
    answer = "".join(answer)
    return answer
