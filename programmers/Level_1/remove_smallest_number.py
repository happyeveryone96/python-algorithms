def solution(arr):
    min_num = min(arr)
    arr.remove(min_num)
    if len(arr) == 0:
        answer = [-1]
    else:
        answer = arr
    return answer
