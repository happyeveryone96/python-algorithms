def solution(x):
    str_num = str(x)
    sum = 0
    for i in range(len(str_num)):
        sum += int(str_num[i])
    if x % sum == 0:
        answer = True
    else:
        answer = False
    return answer
