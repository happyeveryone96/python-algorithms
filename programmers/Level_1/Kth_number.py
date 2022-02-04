def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        copied_arr = array[:]
        first_element = commands[i][0]
        second_element = commands[i][1]
        third_element = commands[i][2]
        new_arr = copied_arr[first_element-1:second_element]
        answer.append(sorted(new_arr)[third_element-1])
    return answer
