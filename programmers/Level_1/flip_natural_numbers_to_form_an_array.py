def solution(n):
    answer = []
    for i in reversed(range(len(str(n)))):
        answer.append(int(str(n)[i]))
    return answer
