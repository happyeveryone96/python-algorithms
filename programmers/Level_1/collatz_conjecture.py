def solution(num):
    answer = 0
    while (num != 1):
        if (num % 2 == 0):
            num = num / 2
            answer += 1
        elif (num % 2 == 1):
            num = num * 3 + 1
            answer += 1
        elif (answer > 500):
            break
    if (answer > 500):
        answer = -1
    return answer
