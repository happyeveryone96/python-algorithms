import math


def solution(n):
    if (float.is_integer(math.sqrt(n))):
        x = math.sqrt(n)
        answer = (x+1) * (x+1)
    else:
        answer = -1
    return answer
