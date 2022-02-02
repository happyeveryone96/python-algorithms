def solution(n):
    answer = 0
    for i in range(n+1):
        if (i != 0 and float.is_integer(n / i) == True):
            answer += i
    return answer
