from math import gcd


def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)
    for i in range(len(arr)):
        if i == 0:
            answer = lcm(arr[i], arr[i+1])
        else:
            answer = lcm(answer, arr[i])
    return answer
