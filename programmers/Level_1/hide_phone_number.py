def solution(phone_number):
    result = []
    num_len = len(phone_number)
    for i in range(num_len):
        if i < num_len-4:
            result.append('*')
        else:
            result.append(phone_number[i])
    answer = ''.join(result)
    return answer
