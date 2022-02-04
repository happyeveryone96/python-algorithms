def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if (float.is_integer(arr[i] / divisor) == True):
            answer.append(arr[i])
    if len(answer) > 0:
        answer = sorted(answer)
    else:
        answer = [-1]
    return answer
